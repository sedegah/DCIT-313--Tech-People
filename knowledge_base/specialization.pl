:- dynamic student_score/2.
:- discontiguous specialization/1.
:- discontiguous calc_score/2.

specialization(computer_vision).
specialization(nlp_ai).
specialization(cloud_systems).
specialization(cyber_defense).
specialization(blockchain_dev).
specialization(data_engineering).
specialization(iot_systems).
specialization(game_dev).
specialization(bioinformatics).
specialization(quantum_computing).
specialization(ar_vr_hci).
specialization(generalist_architect).

calc_score(generalist_architect, Score) :-
    student_score(math_strength, 5),
    student_score(programming_skill, 5),
    student_score(algorithms_interest, 5),
    student_score(linear_algebra, 5),
    student_score(distributed_systems, 5),
    student_score(security_interest, 5),
    Score = 6.0.
calc_score(generalist_architect, 0.0).

calc_score(computer_vision, Score) :-
    student_score(math_strength, Math),
    student_score(programming_skill, Prog),
    student_score(linear_algebra, LA),
    student_score(physics_robotics, Phys),
    Score is (Math * 0.25) + (Prog * 0.25) + (LA * 0.3) + (Phys * 0.2).

calc_score(nlp_ai, Score) :-
    student_score(math_strength, Math),
    student_score(programming_skill, Prog),
    student_score(linguistics, Ling),
    student_score(probabilistic_models, Prob),
    Score is (Math * 0.2) + (Prog * 0.3) + (Ling * 0.3) + (Prob * 0.2).

calc_score(cloud_systems, Score) :-
    student_score(distributed_systems, Dist),
    student_score(infrastructure, Infra),
    student_score(virtualization, Virt),
    student_score(programming_skill, Prog),
    Score is (Dist * 0.3) + (Infra * 0.3) + (Virt * 0.2) + (Prog * 0.2).

calc_score(cyber_defense, Score) :-
    student_score(security_interest, Sec),
    student_score(networking_skill, Net),
    student_score(operating_systems, OS),
    student_score(ethical_hacking, Hack),
    Score is (Sec * 0.3) + (Net * 0.2) + (OS * 0.2) + (Hack * 0.3).

calc_score(blockchain_dev, Score) :-
    student_score(cryptography, Crypto),
    student_score(distributed_systems, Dist),
    student_score(finance_interest, Fin),
    student_score(programming_skill, Prog),
    Score is (Crypto * 0.4) + (Dist * 0.3) + (Fin * 0.1) + (Prog * 0.2).

calc_score(data_engineering, Score) :-
    student_score(statistics, Stat),
    student_score(data_analysis, Data),
    student_score(parallel_computing, Para),
    student_score(math_strength, Math),
    Score is (Stat * 0.3) + (Data * 0.3) + (Para * 0.2) + (Math * 0.2).

calc_score(iot_systems, Score) :-
    student_score(networking_skill, Net),
    student_score(embedded_systems, Emb),
    student_score(sensors_electronics, Sens),
    student_score(programming_skill, Prog),
    Score is (Net * 0.2) + (Emb * 0.4) + (Sens * 0.2) + (Prog * 0.2).

calc_score(game_dev, Score) :-
    student_score(math_strength, Math),
    student_score(programming_skill, Prog),
    student_score(physics_robotics, Phys),
    student_score(graphics_interest, Graph),
    Score is (Math * 0.2) + (Prog * 0.3) + (Phys * 0.2) + (Graph * 0.3).

calc_score(bioinformatics, Score) :-
    student_score(algorithms_interest, Algo),
    student_score(data_analysis, Data),
    student_score(biology_interest, Bio),
    student_score(statistics, Stat),
    Score is (Algo * 0.3) + (Data * 0.2) + (Bio * 0.3) + (Stat * 0.2).

calc_score(quantum_computing, Score) :-
    student_score(math_strength, Math),
    student_score(linear_algebra, LA),
    student_score(quantum_physics, Quant),
    student_score(algorithms_interest, Algo),
    Score is (Math * 0.2) + (LA * 0.3) + (Quant * 0.3) + (Algo * 0.2).

calc_score(ar_vr_hci, Score) :-
    student_score(graphics_interest, Graph),
    student_score(ux_design, UX),
    student_score(app_building, App),
    student_score(sensors_electronics, Sens),
    Score is (Graph * 0.3) + (UX * 0.3) + (App * 0.2) + (Sens * 0.2).

why(computer_vision, 'Your strong foundation in Linear Algebra and Physics makes you ideal for building systems that perceive and interact with the physical world.').
why(nlp_ai, 'Your combined interest in Linguistics and Probabilistic Models suggests a career in developing advanced language models and conversational AI.').
why(cloud_systems, 'Your preference for Distributed Systems and Virtualization aligns perfectly with architecting scalable cloud-native solutions.').
why(cyber_defense, 'Your technical interest in OS internals and ethical hacking is essential for deep-level security auditing and defense.').
why(blockchain_dev, 'Your expertise in Cryptography and Distributed Systems puts you at the forefront of Decentralized Finance (DeFi) and secure ledger tech.').
why(data_engineering, 'Your strength in Parallel Computing and Statistics is critical for managing the massive data pipelines that power modern enterprises.').
why(iot_systems, 'Your skill in Embedded Systems and Sensor integration is key to developing the next generation of smart, connected environments.').
why(game_dev, 'Your passion for Computer Graphics and Physics engines, combined with strong programming, makes you a prime candidate for Game Engine development.').
why(bioinformatics, 'Your interest in Biological data and Algorithmic optimization puts you on the path to discovering medical breakthroughs through computational modeling.').
why(quantum_computing, 'Your mastery of Linear Algebra and Quantum Physics prepares you for the next frontier of computing, solving NP-hard problems with quantum circuits.').
why(ar_vr_hci, 'Your focus on User Experience and Spatial computing makes you an ideal architect for the future of immersive Augmented and Virtual Reality systems.').
why(no_cs_interest, 'Your consistently low interest across all computer science domains suggests that Computer Science may not be the right fit for your academic and career goals. Consider exploring fields that align more closely with your natural interests and strengths.').

job_description(no_cs_interest, 'Career Recommendation: Based on your responses, you may want to consider alternative academic paths such as Business, Arts, Social Sciences, or other fields where you can find more genuine interest and motivation. Computer Science requires strong passion for technology, problem-solving, and continuous learning in rapidly evolving technical domains.').

job_description(computer_vision, 'Roboticist / CV Engineer: You will develop algorithms that allow machines to see and understand the physical world. Core tasks include image processing, 3D reconstruction, and motion planning for autonomous systems.').
job_description(nlp_ai, 'NLP Scientist / AI Architect: You will focus on the computational modeling of human language. Your role involves developing Large Language Models (LLMs), sentiment analysis tools, and machine translation systems.').
job_description(cloud_systems, 'Cloud Architect / DevOps Engineer: You will design and deploy highly available distributed systems. You will work with microservices, Kubernetes, and CI/CD pipelines to ensure scalable infrastructure.').
job_description(cyber_defense, 'Security Researcher / Penetration Tester: You will protect digital assets by identifying and fixing system vulnerabilities. This involves deep-level security auditing, malware analysis, and risk mitigation.').
job_description(blockchain_dev, 'Blockchain Developer / Smart Contract Auditor: You will build secure, decentralized financial systems. You will work with consensus algorithms, smart contracts, and secure ledger technologies.').
job_description(data_engineering, 'Data Engineer / ML Ops: You will architect the massive data pipelines that power modern AI. Your work involves data warehousing, parallel computing, and ensuring data integrity at scale.').
job_description(iot_systems, 'IoT Architect / Embedded Engineer: You will build the next generation of smart, connected environments. You will work with low-level C++ programming, sensor integration, and hardware-software interfacing.').
job_description(game_dev, 'Game Engine Developer / Graphics Researcher: You will build the core technology behind interactive entertainment. You will focus on real-time rendering, shader programming, and high-performance physics simulations.').
job_description(bioinformatics, 'Bioinformatics Scientist / Genomic Researcher: You will apply computer science to the mysteries of life. You will develop algorithms for gene mapping, protein folding, and drug discovery.').
job_description(quantum_computing, 'Quantum Algorithm Researcher / HPC Expert: You will work at the bleeding edge of physics and CS. You will design sub-linear algorithms for quantum systems that outperform classical supercomputers.').
job_description(ar_vr_hci, 'Immersive UX Engineer / AR Architect: You will redefine how humans interact with technology. You will work on spatial computing, gesture recognition, and seamless integration between physical and digital worlds.').
job_description(generalist_architect, 'Chief Technical Architect / Product Leader: You possess a 360-degree technical worldview. You will lead cross-functional teams, bridging the gap between hardware, cloud, AI, and design to build holistic products.').

interest_match(Track, Interest) :-
    mapping(Track, InterestList),
    member(Interest, InterestList),
    student_score(Interest, Val),
    Val > 3.

mapping(computer_vision, [math_strength, linear_algebra, physics_robotics]).
mapping(nlp_ai, [linguistics, probabilistic_models, programming_skill]).
mapping(cloud_systems, [distributed_systems, infrastructure, virtualization]).
mapping(cyber_defense, [security_interest, operating_systems, ethical_hacking]).
mapping(blockchain_dev, [cryptography, distributed_systems, finance_interest]).
mapping(data_engineering, [statistics, data_analysis, parallel_computing]).
mapping(iot_systems, [embedded_systems, sensors_electronics, networking_skill]).
mapping(game_dev, [graphics_interest, physics_robotics, programming_skill]).
mapping(bioinformatics, [biology_interest, algorithms_interest, data_analysis]).
mapping(quantum_computing, [quantum_physics, linear_algebra, math_strength]).
mapping(ar_vr_hci, [ux_design, graphics_interest, app_building]).
mapping(generalist_architect, [programming_skill, math_strength, algorithms_interest]).

specialization(no_cs_interest).

calc_score(no_cs_interest, Score) :-
    findall(Val, student_score(_, Val), Scores),
    length(Scores, Count),
    Count > 0,
    sum_list(Scores, Total),
    Average is Total / Count,
    (Average =< 1.0 -> Score = 10.0 ; Score = 0.0).

recommendation(BestTrack) :-
    findall(Score-Track, (specialization(Track), calc_score(Track, Score)), Scores),
    keysort(Scores, Sorted),
    reverse(Sorted, [MaxScore-BestTrack|_]),
    MaxScore > 2.0.

recommendation(no_cs_interest) :-
    findall(Val, student_score(_, Val), Scores),
    length(Scores, Count),
    Count > 0,
    sum_list(Scores, Total),
    Average is Total / Count,
    Average =< 1.0.

clear_scores :- retractall(student_score(_, _)).
add_score(Trait, Value) :- assertz(student_score(Trait, Value)).
