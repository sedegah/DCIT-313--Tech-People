import customtkinter as ctk
import os
from pyswip import Prolog
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ExpertSystemApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tech People | Advanced KBS Expert System")
        self.geometry("1100x900")

        self.prolog = Prolog()
        self.load_kb()

        self.questions = [
            ("math_strength", "Intelligence", "How strong are your general mathematics and logic skills?"),
            ("programming_skill", "Technical", "How would you rate your general programming proficiency?"),
            ("linear_algebra", "Mathematics", "How comfortable are you with Linear Algebra and Matrix operations?"),
            ("physics_robotics", "Science", "How interested are you in Physics, Kinematics, or Robotics?"),
            ("linguistics", "Language", "Do you have an interest in Linguistics or Natural Language structures?"),
            ("probabilistic_models", "Mathematics", "How interested are you in Probabilistic Models and Bayesian logic?"),
            ("distributed_systems", "Architecture", "Are you interested in Distributed Systems and peer-to-peer networks?"),
            ("infrastructure", "Systems", "How interested are you in Cloud Infrastructure and Servers?"),
            ("virtualization", "Systems", "Do you enjoy working with Virtualization and Containerization (Docker/K8s)?"),
            ("security_interest", "Security", "How interested are you in digital security and asset protection?"),
            ("operating_systems", "Systems", "How interested are you in Operating System internals and Memory management?"),
            ("ethical_hacking", "Security", "Are you interested in Ethical Hacking and Penetration Testing?"),
            ("cryptography", "Mathematics", "How interested are you in Cryptography and Mathematical Security?"),
            ("finance_interest", "Business", "Do you have an interest in Financial Systems or Fintech?"),
            ("statistics", "Mathematics", "How comfortable are you with high-level Statistics?"),
            ("data_analysis", "Data", "Do you enjoy discovering insights from unstructured data?"),
            ("parallel_computing", "Science", "How interested are you in Parallel Computing and large-scale data processing?"),
            ("networking_skill", "Systems", "How interested are you in Network Protocols and Connectivity?"),
            ("embedded_systems", "Hardware", "Do you enjoy low-level programming for Embedded Systems?"),
            ("sensors_electronics", "Hardware", "Are you interested in Sensors, Circuits, and Electronics?"),
            ("graphics_interest", "Visuals", "How interested are you in Computer Graphics and Shader programming?"),
            ("algorithms_interest", "Logic", "Do you enjoy complex Algorithm design and optimization?"),
            ("biology_interest", "Science", "How interested are you in Biology, Genomics, or Medical Science?"),
            ("quantum_physics", "Science", "Are you interested in Quantum Mechanics or high-level Physics?"),
            ("ux_design", "Design", "How much do you value User Experience and Interface design?"),
            ("app_building", "Software", "Do you enjoy building user-facing applications (Mobile/Web)?"),
            ("game_mechanics", "Logic", "Are you interested in Game Mechanics and Physics simulations?"),
            ("bio_stats", "Data", "How interested are you in Biostatistics or large-scale medical data?"),
            ("complexity_theory", "Logic", "Are you interested in Computational Complexity and NP-hard problems?"),
            ("spatial_computing", "Design", "How interested are you in AR/VR and 3D interaction models?")
        ]
        
        self.user_responses = {}
        self.current_step = 0

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self.main_frame, text="CS DEEP SPECIALIZATION EXPERT SYSTEM", font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.grid(row=0, column=0, pady=(40, 5))
        
        self.subtitle_label = ctk.CTkLabel(self.main_frame, text="CREATED BY TECH PEOPLE | DCIT 313 ACADEMIC ADVISORY", font=ctk.CTkFont(size=13, weight="normal"))
        self.subtitle_label.grid(row=1, column=0, pady=(0, 40))

        self.question_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.question_frame.grid(row=2, column=0, sticky="nsew", padx=20)
        self.question_frame.grid_columnconfigure(0, weight=1)

        self.tag_label = ctk.CTkLabel(self.question_frame, text="", font=ctk.CTkFont(size=11, weight="bold"), text_color="#3B8ED0")
        self.tag_label.grid(row=0, column=0, pady=(10, 0))

        self.prompt_label = ctk.CTkLabel(self.question_frame, text="", font=ctk.CTkFont(size=24, weight="bold"), wraplength=800)
        self.prompt_label.grid(row=1, column=0, pady=(10, 30))

        self.slider = ctk.CTkSlider(self.question_frame, from_=0, to=5, number_of_steps=5, width=500)
        self.slider.grid(row=2, column=0, pady=20)
        self.slider.set(2.5)

        self.value_label = ctk.CTkLabel(self.question_frame, text="Response Strength: 3", font=ctk.CTkFont(size=16))
        self.value_label.grid(row=3, column=0)
        self.slider.configure(command=self.update_slider_label)

        self.nav_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.nav_frame.grid(row=3, column=0, pady=40)
        
        self.next_button = ctk.CTkButton(self.nav_frame, text="Next Question", command=self.next_question, width=250, height=50, font=ctk.CTkFont(size=16, weight="bold"))
        self.next_button.grid(row=0, column=0, padx=10)

        self.bind("<Left>", lambda e: self.adjust_slider(-1))
        self.bind("<Right>", lambda e: self.adjust_slider(1))
        self.bind("<Return>", lambda e: self.next_question())
        
        for i in range(6):
            self.bind(str(i), lambda e, val=i: self.set_slider_val(val))
            self.bind(f"<KP_{i}>", lambda e, val=i: self.set_slider_val(val))

        self.show_question()

    def set_slider_val(self, val):
        if self.current_step < len(self.questions):
            self.slider.set(val)
            self.update_slider_label(val)

    def adjust_slider(self, delta):
        if self.current_step < len(self.questions):
            current = self.slider.get()
            new_val = max(0, min(5, current + delta))
            self.slider.set(new_val)
            self.update_slider_label(new_val)

    def update_slider_label(self, val):
        self.value_label.configure(text=f"Response Strength: {int(float(val))}")

    def load_kb(self):
        kb_path = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base', 'specialization.pl')
        kb_path = kb_path.replace('\\', '/')
        try:
            self.prolog.consult(kb_path)
        except Exception as e:
            messagebox.showerror("Logic Error", f"Symbolic Brain Fault: {e}")
            self.destroy()

    def show_question(self):
        if self.current_step < len(self.questions):
            trait, tag, prompt = self.questions[self.current_step]
            self.tag_label.configure(text=tag.upper())
            self.prompt_label.configure(text=prompt)
            self.slider.set(3)
            self.update_slider_label(3)
            
            progress = (self.current_step) / len(self.questions)
            self.title_label.configure(text=f"Deep Assessment: {int(progress*100)}%")
        else:
            self.show_results()

    def next_question(self):
        if self.current_step >= len(self.questions):
            self.show_results()
            return
            
        trait, _, _ = self.questions[self.current_step]
        val = int(self.slider.get())
        self.user_responses[trait] = val
        
        self.current_step += 1
        if self.current_step < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def format_recommendation(self, rec):
        overrides = {
            'nlp_ai': 'NLP & Artificial Intelligence',
            'iot_systems': 'IoT Systems Engineering',
            'cyber_defense': 'Cybersecurity & Defense',
            'cloud_systems': 'Cloud & Distributed Systems',
            'blockchain_dev': 'Blockchain Development',
            'data_engineering': 'Big Data Engineering',
            'game_dev': 'Game Development',
            'bioinformatics': 'Bioinformatics',
            'quantum_computing': 'Quantum Computing',
            'ar_vr_hci': 'AR/VR & Human-Computer Interaction',
            'computer_vision': 'Computer Vision',
            'generalist_architect': 'Technical Architecture',
            'no_cs_interest': 'No Computer Science Interest'
        }
        if rec in overrides: return overrides[rec]
        return " ".join([p.upper() if p.lower() in ['nlp', 'ai', 'iot', 'os', 'hpc', 'ar', 'vr'] else p.capitalize() for p in rec.split('_')])

    def show_results(self):
        list(self.prolog.query("clear_scores"))
        for trait, val in self.user_responses.items():
            self.prolog.assertz(f"student_score({trait}, {val})")

        results = list(self.prolog.query("recommendation(X)"))
        
        self.question_frame.grid_forget()
        self.nav_frame.grid_forget()

        self.main_frame.grid_rowconfigure(2, weight=1)
        result_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        result_frame.grid(row=2, column=0, sticky="nsew", padx=20)
        result_frame.grid_columnconfigure(0, weight=1)

        if results:
            rec = results[0]['X']
            rec_display = self.format_recommendation(rec)
            
            why_res = list(self.prolog.query(f"why({rec}, E)"))
            explanation = why_res[0]['E'] if why_res else ""

            desc_res = list(self.prolog.query(f"job_description({rec}, D)"))
            job_desc = desc_res[0]['D'] if desc_res else ""

            interest_res = list(self.prolog.query(f"interest_match({rec}, I)"))
            interests = [i['I'].replace('_', ' ').title() for i in interest_res]

            ctk.CTkLabel(result_frame, text="DEEP SPECIALIZATION MATCH", font=ctk.CTkFont(size=12, weight="bold"), text_color="#3B8ED0").grid(row=0, column=0, pady=(30, 0))
            ctk.CTkLabel(result_frame, text=rec_display, font=ctk.CTkFont(size=48, weight="bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(10, 40))
            
            reason_card = ctk.CTkFrame(result_frame, fg_color="#1A1A1A", corner_radius=12, border_width=1, border_color="#3B8ED0")
            reason_card.grid(row=2, column=0, sticky="nsew", padx=60, pady=10)
            reason_card.grid_columnconfigure(0, weight=1)
            ctk.CTkLabel(reason_card, text="Symbolic Reasoning & Justification", font=ctk.CTkFont(size=18, weight="bold"), text_color="#3B8ED0").grid(row=0, column=0, pady=(20, 10))
            ctk.CTkLabel(reason_card, text=explanation, font=ctk.CTkFont(size=16), wraplength=700, justify="center").grid(row=1, column=0, pady=(10, 25), padx=40)

            desc_card = ctk.CTkFrame(result_frame, fg_color="#141414", corner_radius=12, border_width=1, border_color="#555555")
            desc_card.grid(row=3, column=0, sticky="nsew", padx=60, pady=10)
            desc_card.grid_columnconfigure(0, weight=1)
            ctk.CTkLabel(desc_card, text="Professional Career Overview", font=ctk.CTkFont(size=18, weight="bold"), text_color="#FFFFFF").grid(row=0, column=0, pady=(20, 10))
            ctk.CTkLabel(desc_card, text=job_desc, font=ctk.CTkFont(size=15), wraplength=700, justify="center", text_color="#CCCCCC").grid(row=1, column=0, pady=(10, 25), padx=40)

            if interests:
                int_card = ctk.CTkFrame(result_frame, fg_color="#101010", corner_radius=12, border_width=1, border_color="#3B8ED0")
                int_card.grid(row=4, column=0, sticky="nsew", padx=60, pady=10)
                int_card.grid_columnconfigure(0, weight=1)
                ctk.CTkLabel(int_card, text="Your Key Interest Drivers", font=ctk.CTkFont(size=18, weight="bold"), text_color="#3B8ED0").grid(row=0, column=0, pady=(20, 10))
                ctk.CTkLabel(int_card, text=" | ".join(interests), font=ctk.CTkFont(size=15), wraplength=700, justify="center", text_color="#AABBCC").grid(row=1, column=0, pady=(10, 25), padx=40)
        else:
            ctk.CTkLabel(result_frame, text="The expert system found no dominant domain Match.", font=ctk.CTkFont(size=20), text_color="#FF4444").grid(row=0, column=0, pady=100)

        ctk.CTkButton(self.main_frame, text="Recalibrate Assessment", command=self.restart, width=250, height=45).grid(row=4, column=0, pady=40)

    def restart(self):
        self.destroy()
        app = ExpertSystemApp()
        app.mainloop()

if __name__ == "__main__":
    app = ExpertSystemApp()
    app.mainloop()
