# save as extract_svg_tables.py
import xml.etree.ElementTree as ET
import json
import sys
from datetime import datetime, timezone

now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

def parse_svg(file_path):
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    tree = ET.parse(file_path)
    root = tree.getroot()
    shapes = []
    for rect in root.findall('.//{http://www.w3.org/2000/svg}rect'):
        data_id = rect.attrib.get('data-table-id') or rect.attrib.get('id')
        shapes.append({
            'table_id': int(data_id) if data_id and str(data_id).isdigit() else data_id,
            'type': 'rect',
            'x': float(rect.attrib.get('x',0)),
            'y': float(rect.attrib.get('y',0)),
            'w': float(rect.attrib.get('width',0)),
            'h': float(rect.attrib.get('height',0)),
            'rx': float(rect.attrib.get('rx',0)) if 'rx' in rect.attrib else 0,
            'svg_id': rect.attrib.get('id', data_id),
        })
    for circ in root.findall('.//{http://www.w3.org/2000/svg}circle'):
        data_id = circ.attrib.get('data-table-id') or circ.attrib.get('id')
        shapes.append({
            'table_id': int(data_id) if data_id and str(data_id).isdigit() else data_id,
            'type':'circle',
            'cx': float(circ.attrib.get('cx',0)),
            'cy': float(circ.attrib.get('cy',0)),
            'r': float(circ.attrib.get('r',0)),
            'svg_id': circ.attrib.get('id', data_id),
        })
    for poly in root.findall('.//{http://www.w3.org/2000/svg}polygon'):
        data_id = poly.attrib.get('data-table-id') or poly.attrib.get('id')
        pts = poly.attrib.get('points','').strip()
        pts_list = []
        for p in pts.split():
            if ',' in p:
                x,y = p.split(',')
                pts_list.append([float(x), float(y)])
        shapes.append({'table_id': int(data_id) if data_id and str(data_id).isdigit() else data_id,
                       'type':'polygon','points': pts_list,
                       'svg_id': poly.attrib.get('id', data_id)})
    return shapes

def shapes_to_workspace_fixtures(shapes):
    fixtures = []
    for i, shape in enumerate(shapes, start=1):
        # Adjust these fields as per your WorkSpace model
        fields = {
            "name": f"Workspace {shape.get('table_id', i)}",
            "svg_id": shape.get('svg_id', f"ws-{i}"),
            "svg_shape": shape['type'],
            "svg_x_coord": int(shape.get('x', shape.get('cx', 0))),
            "svg_y_coord": int(shape.get('y', shape.get('cy', 0))),
            "svg_width": int(shape.get('w', shape.get('r', 0)*2 if shape['type']=='circle' else 0)),
            "svg_height": int(shape.get('h', shape.get('r', 0)*2 if shape['type']=='circle' else 0)),
            "status": "available",
            "location": "Auto-imported",
            "capacity": 4,
            "workspace_type": "desk",
            "description": "",
            "amenities": "",
            "hourly_rate": "0.00",
            "created_at": now,
            "updated_at": now,
        }
        fixtures.append({
            "model": "booking.workspace",
            "pk": i,
            "fields": fields
        })
    return fixtures

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: python svg_parser.py floorplan.svg")
        sys.exit(1)
    shapes = parse_svg(sys.argv[1])
    print(json.dumps(shapes, indent=2))

    # Generate Django fixture
    fixtures = shapes_to_workspace_fixtures(shapes)
    with open("workspace_fixture.json", "w") as f:
        json.dump(fixtures, f, indent=2)
    print("Django fixture written to workspace_fixture.json")