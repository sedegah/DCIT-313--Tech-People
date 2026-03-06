# Knowledge Engineering Report: Advanced Rule-Based Expert System
**Technical Report for DCIT 313: Group Project**  
**Submission for Group: Tech People**

## 1. Introduction: Symbolic AI vs. Literal Code
The primary objective of this project was to implement a system that demonstrates true **Inference**. Unlike standard software that uses nested `if-else` blocks in a procedural language (Python), this system externalizes its "Intelligence" into a **Declarative Knowledge Base**. 

This distinction is critical for the marking rubric:
- **Python**: Acts as the interface actuator, handling I/O and visualization.
- **Prolog**: Acts as the symbolic brain, handling reasoning, conflict resolution, and weighted scoring.

## 2. The Knowledge Engineering Cycle
The transition from human expertise to a digital expert system involved four distinct phases:

### 2.1 Knowledge Acquisition
We analyzed the Computer Science curricula across multiple domains—ranging from Physics-heavy Robotics to Linguistics-heavy NLP. We identified **30+ primitive traits** that distinguish an expert in one track from another.

### 2.2 Knowledge Conceptualization
We mapped these traits into a **Heuristic Weighted Matrix**. We determined that interests are not binary (Yes/No) but continuous (Strength 0-5). 

### 2.3 Knowledge Formalization (Prolog Rules)
We translated these concepts into **Production Rules**. Every specialization track is represented as a predicate that performs a mathematical weighted sum over the available dynamic facts.

### 2.4 Knowledge Verification
The system was stress-tested using "Conflict Scenarios." For instance, if a student likes Math (AI), Algorithms (Bioinformatics), and Shader Programming (Game Dev), the heuristics determine which area has the highest **Relative Salience**.

## 3. Advanced Logical Framework
The system implements several advanced AI patterns to ensure a high-fidelity recommendation.

### A. Weighted Heuristics (Mathematical Symbolic AI)
Each track $Track_k$ uses a formula:
$$Score_k = \sum (Trait_i \times Weight_i)$$
This allows the system to remain robust even when user input is inconsistent or "noisy."

### B. Interest Sensitivity Analysis (`interest_match/2`)
To provide "Human-Like" guidance, the system identifies **Key Driver Traits**. 
- It scans the asserted facts `student_score(T, V)`.
- If $V > 3$ and $T$ is a mapped driver for the chosen $Track_k$, it is flagged as a primary reason for the recommendation.

### C. Explainable AI (XAI) Architecture
The system utilizes the **Declarative Justification Pattern**. By querying `why(Result, Reason)`, the interface can explain the symbolic reasoning behind its decision, satisfying the requirement for transparency.

## 4. Interdisciplinary Foundations
The system architecture reflects the interdisciplinary nature of AI:
- **Logic (Philosophy)**: The use of First-Order Logic (FOL) predicates to represent truth values.
- **Statistics (Math)**: The application of weighted averages to resolve uncertainty.
- **Cognitive Science (Psychology)**: The mimicking of an expert's "Intuition" through the prioritization of certain traits over others (e.g., placing more weight on Linear Algebra for Quantum Computing than on general programming).

5. Logic Integrity Verification
| Test Case | Expected Outcome | Logic Integrity Check |
|-----------|------------------|----------------------|
| High DNA/Bio + High Algo | Bioinformatics | **Bio Mapping** (Algo*0.3 + Bio*0.3) > Threshold |
| High Physics + High Math | Computer Vision | **Physics Priority** (Phys*0.2 + LA*0.3) > Threshold |
| Mixed Weak Scores (All 0s) | No Match Found | **Safety Threshold** (MaxScore < 2.0) Prevents False Advice | 
| All Peak Scores (All 5s) | Generalist Architect | **Salience Overdrive** Logic identifies "T-Shaped" talent. |

## 6. Conclusion
By decoupling the **Knowledge Base** from the **Inference Mechanism**, we have created a system that is not only "code" but a true **Knowledge-Based System**. It honors the principles of Symbolic AI while utilizing modern UI techniques to deliver high-fidelity academic advisory.
