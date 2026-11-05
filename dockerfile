FROM node 
WORKDIR /app
COPY par_impar.js .
CMD ["node", "par_impar.js"]