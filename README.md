# DCIT313 - TechPeople: CS Specialization Expert System

Welcome to the **Advanced Rule-Based Expert System** developed by **Tech People**. This system is designed to provide intelligent academic advisory for Computer Science students at the University of Ghana, helping them select the most suitable specialization track.

---

## Group Members
| Name | 
|------|
| ABDUL SALAM, RABIATU |
| AWAITEY, CHRIS LARBI |
| BOYE, EDMUND NII LARYEA |
| FUSEINI, IYAD-DEEN INUSAH |
| MENDS-BREW, JASON NANA SAM |
| OWUSU-ANSAH, OHENEWAA NANA |
| SEDEGAH, KIMATHI ELIKPLIM KWASHIE |

---

## Project Overview
This project addresses the challenge students face when choosing an academic specialization. Instead of relying on peer influence or limited data, students can use this **Expert System (KBS)** to receive a recommendation based on their unique strengths, interests, and technical skills.

### Key Features:
- **Advanced Logic Engine**: Powered by SWI-Prolog using a weighted scoring system.
- **Explainable AI (XAI)**: Provides clear "Why?" justifications for every recommendation.
- **Modern GUI**: A professional, dark-mode desktop interface built with `CustomTkinter`.
- **Nuanced Assessment**: Evaluates 12 specific technical and logical traits on a 0-5 scale.

---

## System Architecture
The repository is organized following the mandatory project guidelines for DCIT 313:

### 1. Knowledge Base (Intelligence)
- **Path**: `/knowledge_base/specialization.pl`
- **Role**: Memory & Logic.
- **Description**: Contains the symbolic facts and production rules. It uses weighted calculations to determine the best specialization fit.

### 2. Inference Interface (Interaction)
- **Path**: `/interface/main.py`
- **Role**: User Interface & Reasoning Bridge.
- **Description**: A Python application that interacts with the Prolog engine via `pyswip`. It handles input collection, query execution, and result visualization.

### 3. Documentation (Knowledge Acquisition)
- **Path**: `/docs/knowledge_engineering.md`
- **Role**: Technical Report.
- **Description**: Detailed report on the Knowledge Engineering process, logic mappings, and architectural decisions.

---

## Tech Stack
- **Logic Engine**: SWI-Prolog
- **Frontend/UI**: Python 3.x with `CustomTkinter`
- **Logic Bridge**: `pyswip`
- **Version Control**: GitHub

---

## Installation and Setup

### Prerequisites
1. **Python**: Install [Python 3.10+](https://www.python.org/downloads/).
2. **SWI-Prolog**: Install [SWI-Prolog](https://www.swi-prolog.org/download/stable) and ensure it is added to your system environment variables (PATH).

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/[Your-Repo-Link].git
   cd DCIT313-GroupTechPeople-CS-Specialization-Expert-System
   ```
2. Install required Python libraries:
   ```bash
   pip install customtkinter pyswip
   ```
3. Run the application:
   ```bash
   python interface/main.py
   ```

---

## Specialization Tracks Covered
The system currently recommends one of the following tracks:
- **Artificial Intelligence**: Focuses on math, problem-solving, and coding.
- **Software Engineering**: Focuses on application development and system design.
- **Cybersecurity**: Focuses on defense, networking, and cryptography.
- **Data Science**: Focuses on statistics, patterns, and data analysis.
- **Networking**: Focuses on infrastructure and system configuration.

---

## Documentation Reference
For a deep dive into how the "intelligence" was extracted and modeled, please refer to the [Knowledge Engineering Report](file:///c:/Users/Kimat/Desktop/DCIT_313/docs/knowledge_engineering.md).
