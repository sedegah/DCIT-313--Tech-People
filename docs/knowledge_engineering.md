# Advanced Knowledge Engineering Report: CS Specialization Expert System

## 1. Evolution to Advanced KBS
This system has been upgraded from a simple Boolean logic engine (Yes/No) to a **Weighted Symbolic Inference System**. This allows for a more nuanced assessment of student traits, mimicking real-world academic advisory more closely.

## 2. Advanced Knowledge Acquisition
- **Sources**: Academic curricula, track requirements, and weighted heuristics from domain experts.
- **Domain**: Focused on 5 specialized CS tracks with 12 distinct assessment metrics.

## 3. Knowledge Representation (Weighted Logic)
The system uses a **Production Rule System with Certainty Factors (Weights)**.
- **Fact Storage**: `student_score(Trait, Value)` where Value is on a scale of 0-5.
- **Inference Rule**: `calc_score(Track, Score)` calculates a weighted average for each track.
- **Conflict Resolution**: The system uses **Salience** (via `keysort`) to pick the track with the highest calculated score.

### Weighted Mapping Example (AI):
- `math_strength` weight: 40%
- `programming_skill` weight: 30%
- `problem_solving` weight: 30%
- Resulting Score = `(Math * 0.4) + (Prog * 0.3) + (Prob * 0.3)`

## 4. Technical Architecture
- **Inference Engine**: SWI-Prolog (Declarative logic).
- **GUI Layer**: Python with `CustomTkinter` (Modern, asynchronous-friendly UI).
- **Bridge**: `pyswip` (Dynamic FFI between Python and Prolog).

## 5. Logical Justification (The "Why")
Unique to this advanced version is the `why/2` predicate. This provides a symbolic explanation for the recommendation, ensuring the system is not a "black box" but an **Explainable AI (XAI)**.
