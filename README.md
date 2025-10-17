# backSPACE - Workspace Booking System

backSPACE is a Django-based workspace booking system that allows users to book desks, meeting rooms, and collaboration spaces in real-time. The application features an interactive SVG floor plan, CRUD operations for managing bookings, and an admin panel for workspace management.

![Am I Responsive Image] 
<img width="1314" height="765" alt="Screenshot 2025-10-17 at 15 21 25" src="https://github.com/user-attachments/assets/a8b003e9-f89f-404d-becf-57ca564e98d4" />

[View Live Site](https://backspace-c8042b918673.herokuapp.com/) | [View GitHub Repository](https://github.com/sthDINESH/backspace)

---

## TABLE OF CONTENTS
1. [Design & Planning](#design--planning)
    * [User Experience (UX)](#user-experience-ux)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd-design)
    * [Database Schema](#database-schema)
    
2. [Features](#features)
    * [Existing Features](#existing-features)
    * [CRUD Operations](#crud-operations)
    * [Admin Panel](#admin-panel)
    * [Future Implementations](#future-implementations)
    * [Accessibility](#accessibility)

3. [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

4. [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Code Validation](#code-validation)

5. [Bugs](#bugs)

6. [Deployment](#deployment)
    * [Heroku Deployment](#heroku-deployment)
    * [Local Development](#local-development)

7. [Credits](#credits)
    * [Code Used](#code-used)
    * [Content](#content)
    * [AI Usage](#ai-usage)
    * [Acknowledgments](#acknowledgments)

---

## Design & Planning

### User Experience (UX)
The backSPACE booking system was designed with user convenience in mind. The application provides an intuitive interface for browsing available workspaces, making bookings, and managing reservations. The interactive floor plan allows users to visually select their preferred workspace, making the booking process straightforward and engaging.

**Target Audience:**
- Students and professionals needing workspaces
- Teams requiring meeting rooms
- Individuals seeking quiet study spaces

**User Goals:**
- Quickly find and book available workspaces
- View all personal bookings in one place
- Easily modify or cancel existing bookings
- See real-time workspace availability



### User Stories
User stories were created and tracked using GitHub Projects with MoSCoW prioritisation (Must Have, Should Have, Could Have, Won't Have) following Agile methodology.

#### Must Have (Critical - MVP Features)

**Epic 1: User Authentication & Authorisation**
- **US-001:** As a new visitor, I want to create an account with my email and password so that I can book workspace areas and manage my bookings
- **US-002:** As a registered user, I want to log in to my account so that I can access my bookings and make new reservations
- **US-003:** As a logged-in user, I want to log out of my account so that I can secure my account when using shared devices

**Epic 2: Workspace Visualisation & Selection**
- **US-004:** As a user, I want to see an interactive SVG floor plan of the workspace so that I can visually identify and select available spaces
- **US-005:** As a user, I want to click on an available space in the floor plan so that I can proceed to book it

**Epic 3: Booking Management (CRUD)**
- **US-006:** As a logged-in user, I want to book a selected workspace for a specific date and time so that I can reserve my workspace in advance
- **US-007:** As a logged-in user, I want to see a list of all my current and past bookings so that I can keep track of my workspace reservations
- **US-008:** As a logged-in user, I want to modify my existing booking (date, time, or workspace) so that I can adjust my plans if they change
- **US-009:** As a logged-in user, I want to cancel my booking so that I can free up the workspace if I no longer need it

**Epic 4: Core Data Models**
- **US-010:** As a developer, I want to design and implement a robust database schema so that the application can efficiently store and retrieve booking data

**Epic 5: Admin Panel**
- **US-011:** As an administrator, I want to add, edit, and remove workspace areas so that I can keep the floor plan up to date
- **US-012:** As an administrator, I want to view, edit, and cancel any user booking so that I can manage the workspace effectively

#### Should Have (Important but not Critical)

**Epic 6: Enhanced User Experience**
- **US-013:** As a user, I want to see real-time updates of workspace availability so that I don't attempt to book already-reserved spaces
- **US-014:** As a user, I want to know the deadline for modifying bookings so that I can plan accordingly
- **US-015:** As a user, I want to receive notifications when I create, edit, or cancel bookings so that I have confirmation of my actions
- **US-016:** As a user, I want to filter workspaces by type (desk, meeting room, booth) so that I can quickly find the right space for my needs
- **US-017:** As a logged-in user, I want to view and edit my profile information so that I can keep my details up to date

#### Could Have (Desirable)
- **US-018:** As a user, I want to view my complete booking history with pagination so that I can review past workspace usage
- **US-019:** As a user, I want to see amenities available at each workspace (WiFi, monitor, whiteboard) so that I can choose spaces that meet my needs
- **US-020:** As an administrator, I want to set minimum and maximum booking durations so that workspaces are used fairly
- **US-021:** As a user, I want to create recurring bookings (daily, weekly) so that I don't have to book the same space repeatedly

#### Won't Have (Future Considerations)
- **US-022:** Email notifications - Email confirmations and reminders for bookings
- **US-023:** Calendar Integration - Export bookings to Google Calendar/Outlook
- **US-024:** Payment Integration - Paid workspace bookings with Stripe
- **US-025:** Mobile App - Native iOS/Android application
- **US-026:** QR Code Check-in - QR codes for workspace check-in verification

[View Complete User Stories on GitHub Projects](https://github.com/users/sthDINESH/projects/10)


### Wireframes
Wireframes were created using Balsamiq to plan the layout and user flow before development.

**Desktop Wireframes:**
- Home page wireframe
- Floor plan view wireframe
- Booking list wireframe
- Booking form wireframe

**Mobile Wireframes:**
- Responsive layouts for all pages
- Mobile navigation design


Desktop:
![Desktop 1 Wireframe](static/assets/images/Desktop%20.png) ![Desktop 2 Wireframe](static/assets/images/Desktop%202.png)


Tablet:
![Tablet Wireframe](static/assets/images/Tablet.png)



Mobile:

![Mobile Wireframe](static/assets/images/Mobile.png)



### Typography
<img width="1000" height="620" alt="Screenshot 2025-10-17 at 15 11 35" src="https://github.com/user-attachments/assets/9b7a655b-69f1-4093-be7d-43fc6e773893" />

**Primary Font:** Lato
- Used for headings (h1, h2, h3)
- Modern, clean sans-serif typeface
- Weights used: 200 (Extra Light), 300 (Light), 400 (Regular), 700 (Bold), 800 (Extra Bold), 900 (Black)
- Italic variants: 300, 400
- Chosen for its contemporary appearance and excellent readability in headings

**Secondary Font:** Molengo
- Used for body text, paragraphs, and h4 headings
- Selected for legibility and comfortable reading experience
- Weight used: 400 (Regular)
- Applied to body, paragraphs, and secondary headings for content consistency

Both fonts are imported from Google Fonts to ensure consistent rendering across all browsers and devices.



### Colour Scheme
The colour scheme was chosen to create a professional, calming environment suitable for a workspace booking application, using a carefully curated palette of soft, welcoming colors.

![colour Pallette](static/assets/images/backSpace%202.png)
**Primary Colours:**
- **Uranian Blue** `#b5e2faff` - Primary background color for navigation and main interface elements
- **Moonstone** `#0fa3b1ff` - Primary button color for call-to-action elements
- **Atomic Tangerine** `#f7a072ff` - Primary text color for emphasis and headings
- **Tiffany Blue** `#a6d8d4ff` - Highlight color for interactive elements

**Secondary Colours:**
- **Baby Powder** `#f9f7f3ff` - Secondary button color and light background elements
- **Vanilla** `#eddea4ff` - Secondary text color for subtle content
- **Red** `#ff0000` - Reserved/unavailable workspace indicator on floor plan

**Usage:**
- Navigation bar uses Uranian Blue background
- Headings (h1) use Atomic Tangerine for visibility
- Body text uses Molengo font with appropriate color contrast
- Interactive buttons use Moonstone for primary actions
- Reserved workspaces on SVG floor plan display in red

All colour combinations were tested to ensure readability and provide adequate contrast for accessibility.




### Entity Relationship Diagram (ERD) Design
The core of the study space booking system is based on three main entities: **User**, **WorkSpace**, and **Booking**.  
- **User**: Represents a person who can book study spaces (using Django’s built-in User model).
- **WorkSpace**: Represents a bookable room or area in the library.
- **Booking**: Represents a reservation made by a user for a specific study space and time.

Each booking links a user to a study space for a specific time period.  
A user can have many bookings, and a study space can have many bookings.



```
User --------< Booking >-------- WorkSpace
```

- **User** (1) — (M) **Booking**
- **WorkSpace** (1) — (M) **Booking**

This structure allows users to reserve available study spaces and manage their bookings efficiently.

![ERD Diagram](static/assets/images/erd-diagram.png)

credit: dbdiagram.io, https://dbdiagram.io/




### Database Schema
The database structure follows a relational model with three main entities:

```
User (Django built-in)
  ↓ (One-to-Many)
Booking
  ↓ (Many-to-One)
WorkSpace
```

**WorkSpace Model:**
- **Fields:** name, svg_id, svg_shape, svg_x_coord, svg_y_coord, svg_width, svg_height, status, location, capacity, workspace_type, description, amenities, hourly_rate, created_at, updated_at
- Stores information about bookable spaces (desks, meeting rooms, booths)
- Includes SVG coordinates for interactive floor plan positioning
- Tracks availability status (available, maintenance, reserved)

**Booking Model:**
- **Fields:** user (FK), workspace (FK), booking_date, start_time, end_time, status, purpose, notes, created_at, updated_at
- Represents user reservations with date and time slots
- Includes custom validation methods:
  - `clean()` - Validates business hours (8 AM - 10 PM), prevents past bookings, checks for overlapping reservations
  - `can_be_modified()` - Checks if booking is in the future and can be edited
  - `is_past()` - Determines if booking date/time has passed
- Status choices: pending, confirmed, cancelled, completed

**Relationships:**
- User → Booking: One-to-Many (one user can have multiple bookings)
- WorkSpace → Booking: One-to-Many (one workspace can have multiple bookings)

See the ERD diagram above for visual representation of the database structure.

---



## Features

### Existing Features
**Navigation Bar**
- Present on all pages for consistent navigation using Bootstrap 5
- Shows different links based on authentication status:
  - Logged out: Home, Login, SignUp
  - Logged in: Home, My Bookings, User dropdown with Logout
- Fully responsive with mobile hamburger menu
- Active page highlighting for user orientation
- Toast notifications for user feedback (success, error, info messages)

**User Authentication**
- Secure registration and login system using Django Allauth
- Password validation and security features
- Session management with "remember me" functionality
- Login required for booking functionality
- Secure logout with session clearing

**Interactive Floor Plan**
- SVG-based visual representation of workspace layout
- Dynamically generated from workspace database with SVG coordinates
- Colour-coded availability status:
  - Available workspaces (clickable)
  - Reserved workspaces (non-clickable)
  - User's own bookings (editable class)
- Hover effects showing workspace details
- Date and time picker to check availability for specific time slots
- Real-time filtering based on selected date/time

**My Bookings Page**
- Dedicated page showing all user bookings in a simple list format
- Each booking displays: workspace name, date, time range (start - end), and status
- Edit and Delete buttons available for each booking
- Empty state message: "No bookings found" with "Add a Booking" button
- Direct link to workspace list for creating new bookings

**Booking Management**
- View all personal bookings with full details (workspace name, date, time, status)
- Edit booking functionality via modal popup with inline form
- Delete booking functionality with JavaScript confirmation prompt
- Status tracking (pending, confirmed, cancelled, completed)
- AJAX-based update functionality for seamless editing experience


### CRUD Operations
**Create (Implemented)**
- User-friendly booking form with hidden fields populated from floor plan selection
- Date and time pickers with business hour constraints (8 AM - 10 PM)
- Real-time validation and error messages via Django messages framework
- Workspace selection from interactive floor plan
- Fields: workspace, booking_date, start_time, end_time, purpose, notes
- Automatic status set to "confirmed" upon creation
- Success confirmation with redirect to updated floor plan view
- Validation prevents:
  - Past date bookings
  - Bookings outside business hours
  - Overlapping bookings on same workspace
  - Invalid time ranges (end time before start time)

**Read (Implemented)**
- "My Bookings" page showing all user bookings in list format
- Each booking displays: workspace name, date, time range (start - end), status
- Empty state handling with "No bookings found" message
- Direct link to workspace list when no bookings exist
- API endpoints for fetching booking details via JSON (get_booking_details view)
- API endpoints for fetching workspace details via JSON (get_workspace_details view)

**Update (Implemented)**
- Edit booking functionality via modal on My Bookings page
- AJAX POST request to update_booking view
- Returns JSON response with success/error messages
- Pre-filled form loaded dynamically with existing booking data (via get_booking_details)
- Same validation as creation (business hours, overlapping bookings, past dates)
- Error handling with structured JSON error messages
- Status automatically set to "confirmed" upon successful update
- Only booking owner can edit their own bookings (user verification in view)

**Delete (Implemented)**
- Delete booking functionality via cancel_booking view
- JavaScript confirmation prompt on button click
- Hard delete from database (removes booking record)
- Success message: "Booking cancelled" via Django messages
- Error handling: "Error cancelling booking" with exception details
- Only booking owner can delete their own bookings (user verification in view)
- Workspace becomes available again after deletion
- Supports redirect from both workspace floor plan and my_bookings page


### Admin Panel
**Workspace Management**
- Full CRUD operations for workspaces via Django admin interface
- Fields available for editing:
  - Basic info: name, workspace_type, capacity, location, description
  - SVG coordinates: svg_id, svg_shape, svg_x_coord, svg_y_coord, svg_width, svg_height
  - Pricing: hourly_rate
  - Availability: status (available, maintenance, reserved)
  - Amenities: amenities field for listing features
- Bulk actions for multiple workspaces
- List display showing key fields (name, type, status, capacity)
- Search and filter functionality

**Booking Management**
- View all bookings across all users
- List display: user, workspace, booking_date, start_time, end_time, status
- Filter by:
  - User
  - Date (booking_date)
  - Status (pending, confirmed, cancelled, completed)
- Ability to edit booking details (all fields accessible)
- Ability to delete/cancel bookings
- View timestamps (created_at, updated_at)
- Full admin interface for managing all bookings



### Future Implementations
The following features are planned for future releases:

- **Email Notifications:** Automatic confirmation emails and booking reminders
- **Calendar Integration:** Export bookings to Google Calendar or Outlook
- **Recurring Bookings:** Ability to book the same space weekly
- **Payment System:** Integration with Stripe for paid workspaces
- **Mobile App:** Native iOS and Android applications
- **Booking Analytics:** Usage reports and statistics for administrators
- **QR Code Check-in:** Digital check-in system using QR codes


### Accessibility
The following accessibility features have been implemented:

- **Semantic HTML:** Proper use of HTML5 semantic elements including `<nav>`, `<main>`, `<header>`, and `<footer>`
- **ARIA Labels:** Limited ARIA support implemented:
  - `aria-label="Toggle navigation"` on mobile menu button
  - `aria-label="Close"` on modal close buttons
  - `aria-current="page"` on active navigation links
  - `aria-live` and `aria-atomic` on toast messages
- **Keyboard Navigation:** Bootstrap default keyboard accessibility for navigation, forms, and modals
- **Form Labels:** All form inputs have proper `<label>` tags with `for` attributes linking to input IDs
- **Alt Text:** Descriptive alternative text provided for images (logo, hero image)
- **Responsive Design:** Mobile-first Bootstrap responsive design accessible on all device sizes
- **Django Crispy Forms:** Form rendering with built-in accessibility features



## Technologies Used

### Languages Used
- **HTML5** - Structure and content of templates
- **CSS3** - Custom styling and layout
- **JavaScript (ES6)** - Interactive features for floor plan and form handling
- **Python 3.12.8** - Backend logic and Django framework


### Frameworks, Libraries & Programmes Used
**Backend:**
- **Django 4.2.25** - Python web framework
- **Django Allauth 0.57.2** - Authentication system (registration, login, logout)
- **Django Crispy Forms 2.4** - Form rendering with Bootstrap 5 styling
- **Crispy Bootstrap5 0.7** - Bootstrap 5 template pack for Crispy Forms
- **Gunicorn 20.1.0** - WSGI HTTP server for production deployment
- **WhiteNoise 5.3.0** - Static file serving for production
- **Psycopg2 2.9.11** - PostgreSQL database adapter
- **dj-database-url 0.5.0** - Database configuration helper
- **SQLite** - Development database
- **PostgreSQL** - Production database (planned for Heroku deployment)

**Frontend:**
- **Bootstrap 5.3.8** - CSS framework for responsive design (loaded via CDN)
- **Font Awesome 6.x** - Icon library for user interface
- **JavaScript (Vanilla)** - Interactive floor plan, form validation, confirmation dialogues

**Development Tools:**
- **Git** - Version control with meaningful commit messages
- **GitHub** - Code repository, project management, and collaboration
- **VS Code** - Primary development environment
- **Heroku** - Cloud hosting platform (planned deployment)
- **Python venv** - Virtual environment management
- **Django Debug Toolbar** - Development debugging (optional)

**Design Tools:**
- **dbdiagram.io** - Database ERD design and visualisation
- **SVG** - Interactive floor plan creation and editing
- **Chrome DevTools** - Browser-based debugging and responsive testing
- **config/svg_parser.py** - Custom tool to parse SVG floor plans and generate workspace fixtures

**AI Tools:**
- **Claude AI (Anthropic)** - Code generation, debugging, optimisation, and Git workflow guidance
- **GitHub Copilot** - Code suggestions, completions, and unit test generation

---


## Testing

### Manual Testing



### Automated Testing



### Code Validation

#### CSS
<img width="1494" height="821" alt="CSS Validation - BACKSPACE" src="https://github.com/user-attachments/assets/ba5221e9-d9bf-492c-941d-1c426a080461" />


#### HTML
<img width="1492" height="804" alt="HTML Validation - BACKSPACE" src="https://github.com/user-attachments/assets/aec66c3b-d887-4f22-bd9b-b1a37b075a7a" />

#### LightHouse 

Mobile 
<img width="916" height="594" alt="Mobile- BACKSPACE" src="https://github.com/user-attachments/assets/ceb83854-5bb2-44cf-b881-36e389d3773f" />

Desktop
<img width="1009" height="727" alt="Desktop - BACKSPACE" src="https://github.com/user-attachments/assets/8dba250b-48ef-4597-8441-506a284e5041" />



## Bugs

### Fixed Bugs



### Known Bugs


## Deployment


This website is deployed to Heroku from a GitHub repository, the following steps were taken:

### Creating Repository on GitHub
First make sure you are signed into GitHub and go to the code institutes template, which can be found here.
Then click on use this template and select Create a new repository from the drop-down. Enter the name for the repository and click Create repository from template.
Once the repository was created, I clicked the green gitpod button to create a workspace in gitpod so that I could write the code for the site.

### Creating an app on Heroku
After creating the repository on GitHub, head over to heroku and sign in.
On the home page, click New and Create new app from the drop down.
Give the app a name(this must be unique) and select a region I chose Europe as I am in Europe, Then click Create app.

### Create a database
Log into CIdatabase maker
add your email address in input field and submit the form
open database link in your email
paste dabase URL in your DATABASE_URL variable in env.py file and in Heroku config vars

### Deploying to Heroku.
Head back over to heroku and click on your app and then go to the Settings tab
On the settings page scroll down to the config vars section and enter the DATABASE_URL which you will set equal to the PostgresSQL URL, create Secret key this can be anything, CLOUDINARY_URL this will be set to your cloudinary url and finally Port which will be set to 8000.

Then scroll to the top and go to the deploy tab and go down to the Deployment method section and select GitHub and then sign into your account.
Below that in the search for a repository to connect to search box enter the name of your repository that you created on GitHub and click connect
Once it has been connected scroll down to the Manual Deploy and click Deploy branch when it has deployed you will see a view app button below and this will bring you to your newly deployed app.
Please note that when deploying manually you will have to deploy after each change you make to your repository.


### Local Development

#### Forking the Repository
Forking creates a copy of the repository in your own GitHub account, allowing you to make changes without affecting the original project.

1. Log in to GitHub and navigate to the [backSPACE repository](https://github.com/sthDINESH/backspace)
2. Click the "Fork" button in the top right corner of the page
3. Select your GitHub account as the destination for the fork
4. Wait for GitHub to complete the forking process
5. You now have your own copy of the repository in your account


#### Cloning the Repository
Cloning downloads a copy of the repository to your local machine.

1. Navigate to your forked repository on GitHub (or the original repository)
2. Click the green "Code" button
3. Copy the HTTPS URL (e.g., `https://github.com/YOUR-USERNAME/backspace.git`)
4. Open your terminal/command prompt
5. Navigate to the directory where you want to store the project:
   ```bash
   cd /path/to/your/projects
   ```
6. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/backspace.git
   ```
7. Navigate into the project directory:
   ```bash
   cd backspace
   ```


#### Local Setup
Once you've cloned the repository, follow these steps to set up the project locally:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create env.py file in the root directory with:
import os
os.environ.setdefault("SECRET_KEY", "your-secret-key-here")
os.environ.setdefault("DATABASE_URL", "sqlite:///db.sqlite3")
os.environ.setdefault("DEBUG", "True")

# Run migrations
python manage.py migrate

# Load workspace fixtures (optional)
python manage.py loaddata workspace_fixture.json

# Create superuser for admin access
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`


## Credits

### Code Used



### Content



### AI Usage



### Media
 - Photo by Edmond Dantès from Pexels: https://www.pexels.com/photo/woman-in-red-shirt-sitting-at-the-table-4339473/
 - Photo by SHVETS production from Pexels: https://www.pexels.com/photo/women-sitting-on-the-ground-looking-at-the-silver-laptop-9049688/
 - Photo by Edmond Dantès from Pexels: https://www.pexels.com/photo/people-working-in-the-office-8068217/
 - Photo by fauxels from Pexels: https://www.pexels.com/photo/two-women-sitting-in-front-of-computer-3184350/
 - Photo by Antoni Shkraba Studio from Pexels: https://www.pexels.com/photo/people-in-the-office-having-a-meeting-7163354/
 - Photo by Edmond Dantès from Pexels: https://www.pexels.com/photo/a-bearded-man-in-black-suit-working-on-his-laptop-4339866/
 - ChatGPT generated logo/favicon



### Acknowledgments





