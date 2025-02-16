# Use Node.js to build the React app
FROM node:16

WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the React app
COPY . .

# Build the React app
RUN npm run build

# Expose port 3000
EXPOSE 3000

CMD ["npm", "start"]
