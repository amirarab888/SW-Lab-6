const winston = require('winston');
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [new winston.transports.File({ filename: 'combined.log' })]
});

const requestLogger = (req, res, next) => {
    logger.info();
    next();
};

module.exports = { requestLogger };
