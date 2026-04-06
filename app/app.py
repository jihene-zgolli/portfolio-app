from flask import Flask, jsonify
import config
import os
app = Flask(__name__)
@app.route('/')
def accueil():
    return jsonify({
        "message": "Bienvenue sur mon Portfolio DevOps !",
        "auteur": "Jihene Zgolli",
        "titre": "Cloud-Native Engineer | 5G | DevOps"
    })
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "app": config.APP_NAME,
        "version": config.APP_VERSION,
        "env": config.APP_ENV
    })
@app.route('/skills')
def skills():
    return jsonify({
        "auteur": "Jihene Zgolli",
        "competences": {
            "telecom": [
                "5G Core (AMF, SMF, UPF, UDM, NRF)",
                "PS Core", "VoLTE", "Roaming IN/OUT",
                "3GPP Standards", "Diameter", "GTP",
                "NFVI", "MANO", "Telco Cloud",
                "KPI Analysis", "RCA", "SLA Management"
            ],
            "devops": [
                "Docker", "Kubernetes", "GitHub Actions",
                "CI/CD Pipelines", "Bash Scripting"
            ],
            "cloud": [
                "AWS", "Azure", "OpenShift", "Terraform"
            ],
            "scripting": [
                "Bash", "Python", "YAML"
            ],
            "dev": [
                "Angular", "ASP.NET Core",
                "MEAN Stack", "Laravel"
            ],
            "securite": [
                "IBM QRadar SIEM",
                "Analyse de risques",
                "Réponse aux incidents"
            ]
        },
        "experience": "2 ans Huawei Technologies — 5G Core & Telco Cloud",
        "formation": "Ingénieure TIC — SUP'COM Tunis"
    })
@app.route('/info')
def info():
    return jsonify({
        "app": config.APP_NAME,
        "version": config.APP_VERSION,
        "env": config.APP_ENV,
        "technologies": ["Python", "Flask", "Docker", "Kubernetes"],
        "github": "github.com/jihenezgolli/portfolio-app",
        "docker_hub": "hub.docker.com/r/jihenezgolli/portfolio-app"
    })
if __name__ == "__main__":
    print(f"Démarrage de {config.APP_NAME} sur le port {config.PORT}")
    app.run(host='0.0.0.0', port=config.PORT, debug=False)

