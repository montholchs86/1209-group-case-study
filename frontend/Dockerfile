# Use Node.js official image as a base
FROM node:18-alpine

# Set working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Build the Next.js app
RUN npm run build

# Start the Next.js application
CMD ["npm", "start"]