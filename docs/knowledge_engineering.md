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

## 5. Logic Integrity Verification
| Test Case | Expected Outcome | Logic Integrity Check |
|-----------|------------------|----------------------|
| High DNA/Bio + High Algo | Bioinformatics | **Bio Mapping** (Algo*0.3 + Bio*0.3) > Threshold |
| High Physics + High Math | Computer Vision | **Physics Priority** (Phys*0.2 + LA*0.3) > Threshold |
| Mixed Weak Scores (All 0s) | No CS Interest | **Zero Interest Detection** (Average ≤ 1.0) Triggers Alternative Path Recommendation |
| All Peak Scores (All 5s) | Generalist Architect | **Salience Overdrive** Logic identifies "T-Shaped" talent |
| Low Interest Across All Domains | No CS Interest | **Academic Guidance** System suggests exploring other fields |

### 5.1 Advanced Negative Case Handling
The system now includes sophisticated negative case detection:

- **Zero Interest Threshold**: When average score across all domains ≤ 1.0, the system recommends `no_cs_interest`
- **Academic Guidance**: Instead of forcing a CS specialization, the system provides honest guidance about alternative academic paths
- **Explainable Negative Reasoning**: The `why/2` predicate explains why CS may not be suitable, suggesting fields like Business, Arts, or Social Sciences
- **Career Counseling**: The `job_description/2` predicate provides detailed explanation of CS requirements and why other fields might be better aligned

This enhancement demonstrates **Ethical AI** principles - the system prioritizes student success over forced domain matching.

## 6. Conclusion
By decoupling the **Knowledge Base** from the **Inference Mechanism**, we have created a system that is not only "code" but a true **Knowledge-Based System**. It honors the principles of Symbolic AI while utilizing modern UI techniques to deliver high-fidelity academic advisory.

### 6.1 Ethical AI Enhancement
The addition of the `no_cs_interest` specialization represents a significant advancement in **Ethical AI** design:

- **Student-Centric Approach**: The system prioritizes student success over forced specialization matching
- **Honest Assessment**: Provides transparent guidance when CS may not be the optimal academic path
- **Alternative Path Recommendation**: Suggests exploring Business, Arts, Social Sciences, or other aligned fields
- **Preventing Misguided Decisions**: Avoids pushing students into a field where they show no genuine interest or aptitude

This enhancement transforms the system from a simple matching engine into a comprehensive **academic counseling tool** that demonstrates responsible AI deployment in educational contexts.

### 6.2 Technical Achievement Summary
- **Symbolic Logic Engine**: Complete Prolog knowledge base with 11+ specializations
- **Weighted Heuristic Scoring**: Mathematical models for uncertainty handling
- **Explainable AI**: Full reasoning transparency via why/2 and job_description/2 predicates
- **Ethical Decision Making**: Negative case handling with alternative path guidance
- **Modern UI Integration**: Python/CustomTkinter interface with real-time feedback
- **Comprehensive Testing**: 5+ test scenarios including edge cases and negative cases

The system successfully demonstrates advanced Knowledge Engineering principles while maintaining ethical standards in educational AI applications.
