# Marketing and Sales

A Frappe app for managing marketing and sales workflows.

## Features

- **Leads Management**: View and manage leads in a dedicated SPA interface.

## Installation

1. Add the app to your Frappe bench:
   ```bash
   bench get-app https://github.com/phamos-eu/marketingandsales --branch develop
   bench install-app marketingandsales
   ```

2. Restart the bench:
   ```bash
   bench restart
   ```

## Development

### Frontend
The frontend is built using Vue 3, Vite, and Frappe UI. To develop:

1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   yarn install
   ```

3. Start the development server:
   ```bash
   yarn dev
   ```

### Backend
The backend uses Frappe Framework v16. Custom DocTypes and API endpoints can be added under `marketingandsales/`.

## License

AGPL-3.0
