# Soccer Championship API Project

## Introduction

In this project, I used Python with Django, Django ORM and SQLite3 to create an API for organizing a football championship. Each team represents a national selection. To maintain a minimum level of organization, several validations are required.

 [Original repository](https://github.com/Lih3006/soccer-championship-API)



## Routes

| Endpoint               | HTTP Verb | Objective              |
|------------------------|-----------|------------------------|
| `api/teams/`           | POST      | Register a selection   |
| `api/teams/`           | GET       | List selections        |
| `api/teams/<team_id>/` | GET       | Filter selection       |
| `api/teams/<team_id>/` | PATCH     | Update selection       |
| `api/teams/<team_id>/` | DELETE    | Delete selection       |

## Project Details

### Register a Selection (POST)

**Description:**
- Allows the registration of a national selection (team).

**Business Rules:**
- Teams must have unique names.
- The request body should include the team's name and other relevant information.
- Return the newly created team with a unique identifier.

### List Selections (GET)

**Description:**
- Lists all registered national selections (teams).

**Business Rules:**
- Return a list of all registered teams.

### Filter Selection (GET)

**Description:**
- Allows filtering of a national selection (team) based on its unique identifier.

**Business Rules:**
- Return the team details corresponding to the given identifier.
- If the team is not found, return an appropriate error message.

### Update Selection (PATCH)

**Description:**
- Allows updating the information of a national selection (team) based on its unique identifier.

**Business Rules:**
- The request body can include updated team information.
- Return the updated team details.
- If the team is not found, return an appropriate error message.

### Delete Selection (DELETE)

**Description:**
- Allows deleting a national selection (team) based on its unique identifier.

**Business Rules:**
- Delete the team corresponding to the given identifier.
- If the team is not found, return an appropriate error message.

