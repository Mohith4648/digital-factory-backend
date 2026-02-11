name: Angular CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
      # 1. CHECKOUT
      - name: Checkout Code
        uses: actions/checkout@v4

      # 2. INSTALL DEPENDENCIES
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install Dependencies
        run: npm ci

      # 3. CODE QUALITY
      - name: Lint Check
        run: npm run lint

      - name: Type Check (TypeScript)
        run: npx tsc --noEmit

      # 4. RUN UNIT TESTS
      - name: Run Unit Tests
        run: npm test -- --watch=false --browsers=ChromeHeadless

      # 5. BUILD PRODUCTION
      - name: Build Production
        run: npm run build -- --configuration=production

      # 6. BUILD DOCKER IMAGE
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and Push Docker Image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/angular-app:latest

  # 7. PUSH & DEPLOY (Example via SSH)
  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Server via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            docker pull ${{ secrets.DOCKERHUB_USERNAME }}/angular-app:latest
            docker stop angular-app || true
            docker rm angular-app || true
            docker run -d --name angular-app -p 80:80 ${{ secrets.DOCKERHUB_USERNAME }}/angular-app:latest
