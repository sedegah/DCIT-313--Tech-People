% DCIT 313: Deep Specialization Expert System
% Knowledge Base with Multi-Layered Weighted Scoring

:- dynamic student_score/2.

% Core Specializations
specialization(computer_vision).
specialization(nlp_ai).
specialization(cloud_systems).
specialization(full_stack).
specialization(cyber_defense).
specialization(blockchain_dev).
specialization(data_engineering).
specialization(iot_systems).

% 1. Computer Vision & Robotics
calc_score(computer_vision, Score) :-
    student_score(math_strength, Math),
    student_score(programming_skill, Prog),
    student_score(linear_algebra, LA),
    student_score(physics_robotics, Phys),
    Score is (Math * 0.25) + (Prog * 0.25) + (LA * 0.3) + (Phys * 0.2).

% 2. Natural Language Processing (NLP)
calc_score(nlp_ai, Score) :-
    student_score(math_strength, Math),
    student_score(programming_skill, Prog),
    student_score(linguistics, Ling),
    student_score(probabilistic_models, Prob),
    Score is (Math * 0.2) + (Prog * 0.3) + (Ling * 0.3) + (Prob * 0.2).

% 3. Full-Stack Cloud Architecture
calc_score(cloud_systems, Score) :-
    student_score(app_building, App),
    student_score(distributed_systems, Dist),
    student_score(infrastructure, Infra),
    student_score(virtualization, Virt),
    Score is (App * 0.2) + (Dist * 0.3) + (Infra * 0.3) + (Virt * 0.2).

% 4. Cybersecurity & Digital Forensics
calc_score(cyber_defense, Score) :-
    student_score(security_interest, Sec),
    student_score(networking_skill, Net),
    student_score(operating_systems, OS),
    student_score(ethical_hacking, Hack),
    Score is (Sec * 0.3) + (Net * 0.2) + (OS * 0.2) + (Hack * 0.3).

% 5. Blockchain & Fintech
calc_score(blockchain_dev, Score) :-
    student_score(cryptography, Crypto),
    student_score(distributed_systems, Dist),
    student_score(finance_interest, Fin),
    student_score(programming_skill, Prog),
    Score is (Crypto * 0.4) + (Dist * 0.3) + (Fin * 0.1) + (Prog * 0.2).

% 6. Big Data Engineering
calc_score(data_engineering, Score) :-
    student_score(statistics, Stat),
    student_score(data_analysis, Data),
    student_score(parallel_computing, Para),
    student_score(math_strength, Math),
    Score is (Stat * 0.3) + (Data * 0.3) + (Para * 0.2) + (Math * 0.2).

% 7. Internet of Things (IoT)
calc_score(iot_systems, Score) :-
    student_score(networking_skill, Net),
    student_score(embedded_systems, Emb),
    student_score(infrastructure, Infra),
    student_score(sensors_electronics, Sens),
    Score is (Net * 0.2) + (Emb * 0.4) + (Infra * 0.2) + (Sens * 0.2).

% Finding the best recommendation
recommendation(BestTrack) :-
    findall(Score-Track, (specialization(Track), calc_score(Track, Score)), Scores),
    keysort(Scores, Sorted),
    reverse(Sorted, [MaxScore-BestTrack|_]),
    MaxScore > 2.0.

% Deep Justifications
why(computer_vision, 'Computer Vision & Robotics: Your strong foundation in Linear Algebra and Physics makes you ideal for building systems that perceive and interact with the physical world.').
why(nlp_ai, 'Natural Language Processing: Your combined interest in Linguistics and Probabilistic Models suggests a career in developing advanced language models and conversational AI.').
why(cloud_systems, 'Cloud Infrastructure: Your preference for Distributed Systems and Virtualization aligns perfectly with architecting scalable cloud-native solutions.').
why(cyber_defense, 'Cybersecurity & Forensics: Your technical interest in OS internals and ethical hacking is essential for deep-level security auditing and defense.').
why(blockchain_dev, 'Blockchain Development: Your expertise in Cryptography and Distributed Systems puts you at the forefront of Decentralized Finance (DeFi) and secure ledger tech.').
why(data_engineering, 'Big Data Engineering: Your strength in Parallel Computing and Statistics is critical for managing the massive data pipelines that power modern enterprises.').
why(iot_systems, 'Internet of Things (IoT): Your skill in Embedded Systems and Sensor integration is key to developing the next generation of smart, connected environments.').

% Helpers
clear_scores :- retractall(student_score(_, _)).
add_score(Trait, Value) :- assertz(student_score(Trait, Value)).
