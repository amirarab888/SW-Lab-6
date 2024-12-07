import requests
import time
from concurrent.futures import ThreadPoolExecutor
import json
from datetime import datetime


def make_request():
    try:
        response = requests.get('http://localhost:23008/health')
        return {
            'status_code': response.status_code,
            'response': response.json(),
            'timestamp': datetime.now().isoformat()
        }
    except Exception as e:
        return {
            'status_code': 500,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }


def run_load_test(num_requests=100, concurrent_requests=10):
    print(f"Starting load test with {num_requests} total requests, {concurrent_requests} concurrent...")

    results = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(make_request) for _ in range(num_requests)]
        for future in futures:
            result = future.result()
            results.append(result)

    end_time = time.time()
    duration = end_time - start_time

    # Analyze results
    successful_requests = len([r for r in results if r['status_code'] == 200])
    failed_requests = len(results) - successful_requests

    # Get distribution of servers that handled requests
    server_distribution = {}
    for r in results:
        if r.get('response'):
            server = r['response'].get('server', 'unknown')
            server_distribution[server] = server_distribution.get(server, 0) + 1

    # Print summary
    print("\nLoad Test Results:")
    print(f"Total Duration: {duration:.2f} seconds")
    print(f"Requests per second: {num_requests / duration:.2f}")
    print(f"Successful requests: {successful_requests}")
    print(f"Failed requests: {failed_requests}")
    print("\nServer Distribution:")
    for server, count in server_distribution.items():
        print(f"{server}: {count} requests ({count / len(results) * 100:.1f}%)")


if __name__ == "__main__":
    run_load_test()