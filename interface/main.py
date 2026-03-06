import customtkinter as ctk
import os
from pyswip import Prolog
from tkinter import messagebox

# Configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ExpertSystemApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DCIT 313: Deep Specialization Advisor")
        self.geometry("1000x800")

        # Initialize Prolog
        self.prolog = Prolog()
        self.load_kb()

        # Expanded Questions and traits for Deep Specialization
        self.questions = [
            ("math_strength", "Intelligence", "How strong are your general mathematics and logic skills?"),
            ("programming_skill", "Technical", "How would you rate your general programming proficiency?"),
            ("linear_algebra", "Mathematics", "How comfortable are you with Linear Algebra and Matrix operations?"),
            ("physics_robotics", "Science", "How interested are you in Physics, Kinematics, or Robotics?"),
            ("linguistics", "Language", "Do you have an interest in Linguistics or Natural Language structures?"),
            ("probabilistic_models", "Mathematics", "How interested are you in Probabilistic Models and Bayesian logic?"),
            ("app_building", "Software", "Do you enjoy building user-facing software applications?"),
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
            ("embedded_systems", "Hardware", "Do you enjoy low-level programming for Embedded Systems (Microcontrollers)?"),
            ("sensors_electronics", "Hardware", "Are you interested in Sensors, Circuits, and Electronics?"),
        ]
        
        self.user_responses = {}
        self.current_step = 0

        # UI Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Main Container
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self.main_frame, text="CS Deep Specialization Expert System", font=ctk.CTkFont(size=26, weight="bold"))
        self.title_label.grid(row=0, column=0, pady=(30, 10))
        
        self.subtitle_label = ctk.CTkLabel(self.main_frame, text="Group: Tech People - Advanced KBS", font=ctk.CTkFont(size=14))
        self.subtitle_label.grid(row=1, column=0, pady=(0, 30))

        # Question Frame
        self.question_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.question_frame.grid(row=2, column=0, sticky="nsew", padx=20)
        self.question_frame.grid_columnconfigure(0, weight=1)

        self.tag_label = ctk.CTkLabel(self.question_frame, text="", font=ctk.CTkFont(size=12, weight="bold"), text_color="#3B8ED0")
        self.tag_label.grid(row=0, column=0, pady=(10, 0))

        self.prompt_label = ctk.CTkLabel(self.question_frame, text="", font=ctk.CTkFont(size=22), wraplength=700)
        self.prompt_label.grid(row=1, column=0, pady=(10, 20))

        # Slider
        self.slider = ctk.CTkSlider(self.question_frame, from_=0, to=5, number_of_steps=5, width=500)
        self.slider.grid(row=2, column=0, pady=20)
        self.slider.set(2.5)

        self.value_label = ctk.CTkLabel(self.question_frame, text="Response: 3", font=ctk.CTkFont(size=16))
        self.value_label.grid(row=3, column=0)
        self.slider.configure(command=self.update_slider_label)

        # Navigation Buttons
        self.nav_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.nav_frame.grid(row=3, column=0, pady=40)
        
        self.next_button = ctk.CTkButton(self.nav_frame, text="Next Question", command=self.next_question, width=250, height=50, font=ctk.CTkFont(size=16, weight="bold"))
        self.next_button.grid(row=0, column=0, padx=10)

        self.show_question()

    def update_slider_label(self, val):
        self.value_label.configure(text=f"Response Strength: {int(float(val))}")

    def load_kb(self):
        kb_path = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base', 'specialization.pl')
        kb_path = kb_path.replace('\\', '/')
        try:
            self.prolog.consult(kb_path)
        except Exception as e:
            messagebox.showerror("System Error", f"Critical logic failure: {e}")
            self.destroy()

    def show_question(self):
        if self.current_step < len(self.questions):
            trait, tag, prompt = self.questions[self.current_step]
            self.tag_label.configure(text=tag.upper())
            self.prompt_label.configure(text=prompt)
            self.slider.set(3)
            self.update_slider_label(3)
            
            # Update progress
            progress = (self.current_step) / len(self.questions)
            self.title_label.configure(text=f"Deep Assessment: {int(progress*100)}%")
        else:
            self.show_results()

    def next_question(self):
        trait, _, _ = self.questions[self.current_step]
        val = int(self.slider.get())
        self.user_responses[trait] = val
        
        self.current_step += 1
        if self.current_step < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        list(self.prolog.query("clear_scores"))
        for trait, val in self.user_responses.items():
            self.prolog.assertz(f"student_score({trait}, {val})")

        results = list(self.prolog.query("recommendation(X)"))
        
        self.question_frame.grid_forget()
        self.nav_frame.grid_forget()

        result_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        result_frame.grid(row=2, column=0, sticky="nsew", padx=20)
        result_frame.grid_columnconfigure(0, weight=1)

        if results:
            rec = results[0]['X']
            rec_display = rec.replace('_', ' ').title()
            
            why_results = list(self.prolog.query(f"why({rec}, E)"))
            explanation = why_results[0]['E'] if why_results else "No specific justification provided."

            ctk.CTkLabel(result_frame, text="DEEP SPECIALIZATION MATCH:", font=ctk.CTkFont(size=14, weight="bold"), text_color="#3B8ED0").grid(row=0, column=0, pady=(20, 0))
            ctk.CTkLabel(result_frame, text=rec_display, font=ctk.CTkFont(size=44, weight="bold"), text_color="#FFFFFF").grid(row=1, column=0, pady=(10, 30))
            
            card = ctk.CTkFrame(result_frame, fg_color="#1F1F1F", corner_radius=12, border_width=1, border_color="#3B8ED0")
            card.grid(row=2, column=0, sticky="nsew", padx=50, pady=10)
            card.grid_columnconfigure(0, weight=1)
            
            ctk.CTkLabel(card, text="Symbolic Reasoning & Justification", font=ctk.CTkFont(size=18, weight="bold"), text_color="#3B8ED0").grid(row=0, column=0, pady=(20, 10))
            ctk.CTkLabel(card, text=explanation, font=ctk.CTkFont(size=16), wraplength=600, justify="center").grid(row=1, column=0, pady=(10, 25), padx=30)
        else:
            ctk.CTkLabel(result_frame, text="The assessment found no dominant specialization. You may have a generalist profile.", font=ctk.CTkFont(size=20)).grid(row=0, column=0, pady=100)

        ctk.CTkButton(self.main_frame, text="Recalibrate Assessment", command=self.restart, width=250, height=45).grid(row=4, column=0, pady=40)

    def restart(self):
        self.destroy()
        app = ExpertSystemApp()
        app.mainloop()

if __name__ == "__main__":
    app = ExpertSystemApp()
    app.mainloop()
