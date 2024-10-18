# docker-images
Docker Images


# Generate docker image and run the container
docker build -t flask-web flask-web

# Run the container
docker run -p 8000:8000 flask-web

# Trivy
trivy image flask-web 
trivy image flask-web --exit-code 0 --format sarif > trivy-results.sarif

# Checkov
checkov --framework=dockerfile -f flask-web/Dockerfile -o sarif

# Grype
grype docker:flask-web
