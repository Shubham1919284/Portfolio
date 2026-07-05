import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Replace Projects Section (lines 387 to 511, 0-indexed: 387 to 511)
# Note: PowerShell output said 388 to 513. Let's find exactly the start and end indices.
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<section id="projects" class="projects">' in line:
        start_idx = i
    if '<section id="contact" class="contact">' in line:
        end_idx = i
        break

projects_html = '''    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Featured Projects</h2>
                <div style="width: 50px; height: 3px; background: #0056b3; margin: 0 auto 1.5rem;"></div>
                <p class="section-subtitle">A selection of my recent data-driven and machine learning projects.</p>
            </div>
            
            <div class="projects-grid">
                
                <!-- Project 1 -->
                <div class="project-card" data-modal="modal-blackfriday" style="cursor: pointer;">
                    <div class="project-header" style="justify-content: center; text-align: center; margin-bottom:1rem;">
                        <i class="fas fa-shopping-cart" style="font-size: 3rem; color: #0056b3;"></i>
                    </div>
                    <h3 style="margin-top:1.5rem; margin-bottom:1rem; font-size:2rem; text-align:center;">Black Friday Purchase Prediction</h3>
                    <div class="project-section">
                        <p style="margin-bottom: 2rem; color:#8892b0; text-align:center;">
                            End-to-end regression modeling to predict consumer purchase amounts based on demographic and product features.
                        </p>
                    </div>
                    <div class="project-tech" style="display: flex; gap:1rem; flex-wrap:wrap; font-size:1.2rem; justify-content:center;">
                        <span class="tech-tag">Python</span>
                        <span class="tech-tag">XGBoost</span>
                        <span class="tech-tag">Pandas</span>
                        <span class="tech-tag">Streamlit</span>
                    </div>
                </div>

                <!-- Project 2 -->
                <div class="project-card" data-modal="modal-telecom" style="cursor: pointer;">
                    <div class="project-header" style="justify-content: center; text-align: center; margin-bottom:1rem;">
                        <i class="fas fa-chart-line" style="font-size: 3rem; color: #0056b3;"></i>
                    </div>
                    <h3 style="margin-top:1.5rem; margin-bottom:1rem; font-size:2rem; text-align:center;">Telecom Customer Churn Analysis</h3>
                    <div class="project-section">
                        <p style="margin-bottom: 2rem; color:#8892b0; text-align:center;">
                            Exploratory Data Analysis (EDA) on a telecommunications dataset to uncover hidden drivers behind customer churn.
                        </p>
                    </div>
                    <div class="project-tech" style="display: flex; gap:1rem; flex-wrap:wrap; font-size:1.2rem; justify-content:center;">
                        <span class="tech-tag">Python</span>
                        <span class="tech-tag">Seaborn</span>
                        <span class="tech-tag">Matplotlib</span>
                        <span class="tech-tag">EDA</span>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Modals Overlay -->
    <div class="modal-overlay" id="modalOverlay">
        
        <!-- Black Friday Modal -->
        <div class="modal-content" id="modal-blackfriday" style="display: none;">
            <button class="modal-close"><i class="fas fa-times"></i></button>
            <div class="modal-body">
                <h2 style="font-size:2.8rem; margin-bottom: 1rem;">Black Friday Purchase Prediction</h2>
                <div class="modal-subtitle" style="color: #64ffda; margin-bottom: 2.5rem; font-family: monospace;">Predictive Regression Modeling • XGBoost • Streamlit</div>
                
                <div class="modal-section" style="margin-bottom: 2rem;">
                    <h3 style="font-size:2rem; margin-bottom: 1rem;"><i class="fas fa-exclamation-circle" style="color: #0056b3;"></i> The Pain Point</h3>
                    <p style="color:#8892b0; line-height:1.6;">During massive retail events like Black Friday, retailers struggle to forecast individual customer spending accurately. Without precise prediction, inventory management suffers and targeted marketing campaigns fail to optimize ROI.</p>
                </div>
                
                <div class="modal-section" style="margin-bottom: 2rem;">
                    <h3 style="font-size:2rem; margin-bottom: 1rem;"><i class="fas fa-bullseye" style="color: #0056b3;"></i> Why We Did This</h3>
                    <p style="color:#8892b0; line-height:1.6;">The goal was to build a highly accurate regression model that learns from historical demographics and product categories to predict exact purchase amounts. This empowers businesses to dynamically adjust pricing and personalize offers.</p>
                </div>
                
                <div class="modal-section" style="margin-bottom: 2rem;">
                    <h3 style="font-size:2rem; margin-bottom: 1rem;"><i class="fas fa-chart-pie" style="color: #0056b3;"></i> Impact & Metrics</h3>
                    <ul style="color:#8892b0; line-height:1.6; padding-left:2rem;">
                        <li style="margin-bottom:0.8rem;">Performed EDA and feature engineering on <strong>550K+ retail transaction records</strong> from the Black Friday Kaggle dataset.</li>
                        <li style="margin-bottom:0.8rem;">Implemented preprocessing pipelines with categorical encoding and missing value imputation.</li>
                        <li style="margin-bottom:0.8rem;">Trained and compared 5 regression models; <strong>XGBoost</strong> achieved best performance (<strong>R² = 0.6712, RMSE = 2878.57</strong>).</li>
                        <li style="margin-bottom:0.8rem;">Developed a <strong>Streamlit</strong> app for real-time purchase amount prediction based on customer and product inputs.</li>
                    </ul>
                </div>
                <div style="margin-top:2rem;">
                    <a href="https://github.com/Shubham1919284" target="_blank" class="btn btn-primary" style="text-decoration:none;"><i class="fab fa-github"></i> View Repository</a>
                </div>
            </div>
        </div>

        <!-- Telecom Churn Modal -->
        <div class="modal-content" id="modal-telecom" style="display: none;">
            <button class="modal-close"><i class="fas fa-times"></i></button>
            <div class="modal-body">
                <h2 style="font-size:2.8rem; margin-bottom: 1rem;">Telecom Customer Churn Analysis</h2>
                <div class="modal-subtitle" style="color: #64ffda; margin-bottom: 2.5rem; font-family: monospace;">Exploratory Data Analysis • Statistical Correlation • Data Visualization</div>
                
                <div class="modal-section" style="margin-bottom: 2rem;">
                    <h3 style="font-size:2rem; margin-bottom: 1rem;"><i class="fas fa-exclamation-circle" style="color: #0056b3;"></i> The Pain Point</h3>
                    <p style="color:#8892b0; line-height:1.6;">Customer retention is a critical challenge for telecom companies. High churn rates directly erode revenue, and without understanding <em>why</em> customers leave, companies cannot effectively allocate retention budgets.</p>
                </div>
                
                <div class="modal-section" style="margin-bottom: 2rem;">
                    <h3 style="font-size:2rem; margin-bottom: 1rem;"><i class="fas fa-bullseye" style="color: #0056b3;"></i> Why We Did This</h3>
                    <p style="color:#8892b0; line-height:1.6;">To identify the hidden behavioral and contractual drivers causing customers to drop off. By pinpointing exact demographics and contract types prone to churn, the business can proactively target at-risk users.</p>
                </div>
                
                <div class="modal-section" style="margin-bottom: 2rem;">
                    <h3 style="font-size:2rem; margin-bottom: 1rem;"><i class="fas fa-chart-pie" style="color: #0056b3;"></i> Impact & Metrics</h3>
                    <ul style="color:#8892b0; line-height:1.6; padding-left:2rem;">
                        <li style="margin-bottom:0.8rem;">Conducted end-to-end EDA on <strong>7,000+ telecom customer records</strong> to identify churn drivers across contract type, tenure, and billing.</li>
                        <li style="margin-bottom:0.8rem;">Found month-to-month customers churned at <strong>3× the rate</strong> of annual contract holders — directly informing retention strategy.</li>
                        <li style="margin-bottom:0.8rem;">Produced highly effective <strong>Matplotlib and Seaborn</strong> visualizations highlighting the top 5 factors affecting customer retention.</li>
                    </ul>
                </div>
                <div style="margin-top:2rem;">
                    <a href="https://github.com/Shubham1919284" target="_blank" class="btn btn-primary" style="text-decoration:none;"><i class="fab fa-github"></i> View Repository</a>
                </div>
            </div>
        </div>

    </div>

'''

if start_idx != -1 and end_idx != -1:
    lines[start_idx:end_idx] = [projects_html]

# 2. Add Solitaire Experience
solitaire_html = '''                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <div class="timeline-date">Jan 2026 – Jun 2026</div>
                        <h3>Data Science Trainee</h3>
                        <h4>Solitaire Infosys Pvt. Ltd. <span class="location">– Mohali, Punjab</span></h4>
                        <ul class="timeline-achievements">
                            <li>✅ Cleaned and preprocessed portions of a telecom client's dataset as part of a collaborative team effort</li>
                            <li>✅ Assisted in identifying key columns relevant for churn analysis on the processed data</li>
                            <li>✅ Gained hands-on exposure to real client data handling in a professional setting</li>
                        </ul>
                        <div class="timeline-skills">
                            <span class="skill-tag">Data Cleaning</span>
                            <span class="skill-tag">EDA</span>
                            <span class="skill-tag">Data Science</span>
                        </div>
                    </div>
                </div>
'''

timeline_idx = -1
for i, line in enumerate(lines):
    if '<div class="timeline">' in line:
        timeline_idx = i
        break

if timeline_idx != -1:
    lines.insert(timeline_idx + 1, solitaire_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
