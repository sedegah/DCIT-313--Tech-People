# DCIT313 Technical Design: Advanced Rule-Based Expert System
**Reference Repository**: [https://github.com/sedegah/DCIT-313--Tech-People](https://github.com/sedegah/DCIT-313--Tech-People)

This repository contains a high-fidelity Knowledge-Based System (KBS) designed to facilitate academic track selection for Computer Science students. The system implements a decoupled architecture, separating the symbolic logic engine (SWI-Prolog) from the modern graphical interface (Python).

---

## Group Members
| Name | Role |
|------|------|
| FUSEINI, IYAD-DEEN INUSAH | Group Leader and Data Modeler |
| SEDEGAH, KIMATHI ELIKPLIM KWASHIE |Software Developer and Knowledge Engineer |
| ABDUL SALAM, RABIATU | Systems Analyst |
| AWAITEY, CHRIS LARBI | Technical Architect |
| BOYE, EDMUND NII LARYEA | Logic Designer |
| MENDS-BREW, JASON NANA SAM | Research Lead |
| OWUSU-ANSAH, OHENEWAA NANA | Documentation Lead |

---

## System Architecture and Design Patterns

The system adheres to a strict separation of concerns between the **Memory/Intelligence** and **User Interaction** layers.

### 1. Symbolic Logic Engine (Prolog)
The "Brain" of the system is residing in `knowledge_base/specialization.pl`.
- **Reasoning Method**: Forward Chaining (Data-driven inference).
- **Knowledge Representation**: Production rules paired with a weighted scoring mechanism.
- **Predicates**:
    - `student_score(Trait, Value)`: Dynamic fact storage for user inputs (0-5 scale).
    - `calc_score(Specialization, Score)`: Calculates a weighted average based on specific heuristics.
    - `why(Specialization, Reason)`: Symbolic justification predicate for Explainable AI (XAI) output.

### 2. Inference Interface (Python Bridge)
The "Actuator" resides in `interface/main.py`.
- **Library**: `pyswip` (Dynamic Foreign Function Interface).
- **GUI Framework**: `CustomTkinter` (Modern, asynchronous design).
- **Workflow**:
    1. Python initializes a Prolog thread.
    2. User inputs are collected via a slider-based interface.
    3. Facts are asserted into the Prolog global database via `prolog.assertz`.
    4. Python executes the `recommendation(X)` query.
    5. Results are back-fed into the GUI for visualization.

---

## Mathematical Modeling: Weighted Scoring System

Unlike standard Boolean expert systems, this implementation utilizes a weighted sum model to provide more granular accuracy.

### Formula:
Score for Specialization $S$ is calculated as:
$$Score(S) = \sum_{i=1}^{n} (Trait_i \times Weight_i)$$

### Example Weights (AI Track):
- **Mathematics Strength**: 0.4 (40%)
- **Programming Skill**: 0.3 (30%)
- **Problem Solving**: 0.3 (30%)

This model ensures that even if a student marks a '3' in math but a '5' in programming, the system balances these inputs to find the most mathematically probable track.

---

## Mandatory Project Structure

| Component | Directory | Purpose | AI Role |
|-----------|-----------|---------|---------|
| **Knowledge Base** | `/knowledge_base` | Logical Facts and Rules (.pl) | Memory/Intelligence |
| **Inference Interface** | `/interface` | Python logic and GUI (.py) | User Interaction |
| **Documentation** | `/docs` | Knowledge Engineering Report (.md) | Knowledge Acquisition |

---

## Deployment and Installation

### Hardware/Software Requirements
- **OS**: Windows/Linux/MacOS
- **Interpreter**: Python 3.10+
- **Logic Engine**: SWI-Prolog (Must be in System PATH)

### Installation
```bash
# Clone the repository
git clone https://github.com/sedegah/DCIT-313--Tech-People.git

# Install dependencies
pip install customtkinter pyswip
```

### Critical Note on SWI-Prolog PATH
The `pyswip` library requires the SWI-Prolog DLL to be accessible. Ensure that the directory containing `libswipl.dll` (e.g., `C:\Program Files\swipl\bin`) is added to your environment `PATH`.

---

## Validation and Logic Integrity
The system was verified against 25+ test cases, covering:
- **Positive Correlations**: Strong math + strong logic correctly yielding AI.
- **Edge Cases**: Middle-of-the-road scores (3/5) triggering fallback "Undecided" recommendations if weights do not meet the minimum confidence threshold ($> 1.5$).
- **Conflict Resolution**: Utilization of `keysort` and `reverse` predicates to prioritize the highest-scoring track when multiple conditions are partially met.
