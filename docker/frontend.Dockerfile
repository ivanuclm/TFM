FROM node:20-alpine

WORKDIR /workspace/movilidad-urbana-sim/frontend

COPY movilidad-urbana-sim/frontend/package*.json ./
RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
