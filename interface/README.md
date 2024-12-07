# Interface Service - Load Balancer Implementation

## Project Structure
```
interface/
├── src/
│   ├── server.js           # Main application
│   ├── routes/
│   ├── middleware/
│   │   ├── errorHandler.js
│   │   └── requestLogger.js
│   └── config/
│       └── nginx.conf
├── tests/
│   └── load-test.sh
├── Dockerfile
└── docker-compose.yml
```

## Prerequisites
- Docker & Docker Compose
- Node.js
- Nginx

## Setup Instructions

1. Clone and Setup:
```bash
git clone https://github.com/amirarab888/SW-Lab-6.git
cd SW-Lab-6
git checkout -b interface-layer
```

2. Install Dependencies:
```bash
cd interface
npm install express cors winston
```

3. Start Services:
```bash
docker-compose up -d
```

4. Verify Setup:
```bash
curl localhost:8080/health
docker ps | grep interface
```

## Implementation Details

### Load Balancer
- Uses Nginx for request distribution
- Round-robin algorithm
- Health checks enabled
- Multiple backend instances

### Logging
- Request logging using Winston
- Error handling middleware
- Access and error logs in /logs

### Scaling
- Multiple backend instances
- Container orchestration via Docker Compose
- Easy horizontal scaling

- ![image](https://github.com/user-attachments/assets/f4750bd8-cc90-42e4-b83d-5ef397d727e8)


## Testing

1. Basic Health Check:
```bash
./tests/load-test.sh
```

2. Load Testing:
```bash
ab -n 1000 -c 100 http://localhost:8080/health
```

## Configuration

### Port Mappings:
- Interface: 8080:80
- Backend1: 3001:3000
- Backend2: 3002:3000
- Backend3: 3003:3000

### Environment Variables:
- PORT: Server port (default: 3000)
- LOG_LEVEL: Winston log level

## Troubleshooting

1. Port conflicts:
```bash
sudo lsof -i :8080
sudo kill -9 <PID>
```

2. Container issues:
```bash
docker-compose down
docker-compose up -d
```

## Requirements Met
- RESTful API interface ✓
- Load balancing ✓
- Multiple backend instances ✓
- Shared database configuration ✓
- Docker containerization ✓
- Request logging ✓
- Error handling ✓
- Health monitoring ✓


![image](https://github.com/user-attachments/assets/3251aac9-42c2-4c5f-b587-cd5202cc8268)

![image](https://github.com/user-attachments/assets/e31c78ad-a22c-41f0-9a11-a4d81c9a83ba)

با ران کردن داکر کامپوز تغییر یافته مشاهده می‌شود که سه بکند اجرا شده و دیتابیس اجرا شده و nginx بالا آمده و درخواست‌ها با این که به 23008 رفته و توسط nginx که همان interface سیستم است, بین سرورهای بکند تقسیم می‌شوند.

![Uploading image.png…]()
