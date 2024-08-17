# USCF-Stats

- This project is a web project that displays player information from the [United States Chess Federation - Member Services Area Website](https://www.uschess.org/msa/MbrDtlMain.php?12743305)

## Set Up

### Prequisites

Make sure that you have Python, Pip and Node.js installed

### Backend

#### Install Required Packages

- Run `python3 -m venv .venv` to set up a Python virtual environment
- Activate the virtual environment

  - If on Windows: `.venv\Scripts\activate`
  - If on macOS/Linux: `source .venv/bin/activate`

- Run `pip install Flask`
- Run `pip install BeautifulSoup4`
- Run `pip install requests`
- Run `pip install jsonify`
- Run `pip install lxml`

### Frontend

#### Install Required Packages

Run `npm i`

## Run Application

In your terminal, run `cd backend`
Run `flask run`

In a seperate terminal, run `npm run dev`
