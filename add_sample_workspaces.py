"""
Script to add sample workspaces to the database for testing
Run with: python manage.py shell < add_sample_workspaces.py
"""

from booking.models import WorkSpace

# Sample workspaces
workspaces_data = [
    {
        'name': 'Desk-A1',
        'location': 'Ground Floor',
        'capacity': 1,
        'workspace_type': 'desk',
        'description': 'Hot desk near window',
        'svg_id': 'desk-a1',
        'svg_shape': 'rect',
        'svg_x_coord': 100,
        'svg_y_coord': 100,
        'svg_width': 80,
        'svg_height': 60,
        'status': 'available',
        'amenities': 'WiFi, Monitor, Power outlet',
        'hourly_rate': 5.00,
    },
    {
        'name': 'Desk-A2',
        'location': 'Ground Floor',
        'capacity': 1,
        'workspace_type': 'desk',
        'description': 'Hot desk by entrance',
        'svg_id': 'desk-a2',
        'svg_shape': 'rect',
        'svg_x_coord': 200,
        'svg_y_coord': 100,
        'svg_width': 80,
        'svg_height': 60,
        'status': 'available',
        'amenities': 'WiFi, Power outlet',
        'hourly_rate': 5.00,
    },
    {
        'name': 'Meeting Room 1',
        'location': 'First Floor',
        'capacity': 6,
        'workspace_type': 'meeting',
        'description': 'Conference room with projector',
        'svg_id': 'meeting-1',
        'svg_shape': 'rect',
        'svg_x_coord': 400,
        'svg_y_coord': 200,
        'svg_width': 150,
        'svg_height': 100,
        'status': 'available',
        'amenities': 'WiFi, Projector, Whiteboard, Conference phone',
        'hourly_rate': 15.00,
    },
    {
        'name': 'Pod-1',
        'location': 'Ground Floor',
        'capacity': 4,
        'workspace_type': 'pod',
        'description': 'Collaboration pod',
        'svg_id': 'pod-1',
        'svg_shape': 'rect',
        'svg_x_coord': 300,
        'svg_y_coord': 300,
        'svg_width': 100,
        'svg_height': 80,
        'status': 'available',
        'amenities': 'WiFi, Whiteboard',
        'hourly_rate': 10.00,
    },
]

# Create workspaces
created_count = 0
for data in workspaces_data:
    workspace, created = WorkSpace.objects.get_or_create(
        name=data['name'],
        defaults=data
    )
    if created:
        created_count += 1
        print(f"✅ Created: {workspace.name}")
    else:
        print(f"⏭️  Already exists: {workspace.name}")

print(f"\n🎉 Total workspaces created: {created_count}")
print(f"📊 Total workspaces in database: {WorkSpace.objects.count()}")
