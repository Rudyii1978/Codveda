"""
API Integration Script
A Python script that interacts with an external API to fetch and display data.
This script uses the JSONPlaceholder API (a free fake API for testing).
"""

import json
try:
    import urllib.request
    import urllib.error
except ImportError:
    print("Error: urllib is required but not available.")
    exit(1)

class APIClient:
    """Client for interacting with the JSONPlaceholder API."""
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        """Initialize the API client."""
        self.timeout = 10
    
    def fetch_data(self, endpoint):
        """
        Fetch data from the API endpoint.
        
        Args:
            endpoint: The API endpoint to fetch data from
            
        Returns:
            The JSON response data
            
        Raises:
            Exception: If the request fails
        """
        url = f"{self.BASE_URL}/{endpoint}"
        
        try:
            with urllib.request.urlopen(url, timeout=self.timeout) as response:
                if response.status == 200:
                    data = response.read().decode('utf-8')
                    return json.loads(data)
                else:
                    raise Exception(f"API request failed with status code: {response.status}")
        except urllib.error.URLError as e:
            raise Exception(f"Network error: {e.reason}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse JSON response: {e}")
    
    def get_posts(self, limit=10):
        """Fetch a list of posts."""
        posts = self.fetch_data("posts")
        return posts[:limit] if limit else posts
    
    def get_post(self, post_id):
        """Fetch a single post by ID."""
        return self.fetch_data(f"posts/{post_id}")
    
    def get_users(self):
        """Fetch a list of users."""
        return self.fetch_data("users")
    
    def get_user(self, user_id):
        """Fetch a single user by ID."""
        return self.fetch_data(f"users/{user_id}")
    
    def get_comments(self, post_id=None, limit=10):
        """Fetch comments, optionally for a specific post."""
        if post_id:
            comments = self.fetch_data(f"posts/{post_id}/comments")
        else:
            comments = self.fetch_data("comments")
        return comments[:limit] if limit else comments

def display_posts(posts):
    """Display posts in a formatted way."""
    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'User ID':<10} {'Title':<65}")
    print("=" * 80)
    
    for post in posts:
        title = post['title'][:60] + "..." if len(post['title']) > 60 else post['title']
        print(f"{post['id']:<5} {post['userId']:<10} {title:<65}")
    
    print("=" * 80)

def display_users(users):
    """Display users in a formatted way."""
    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'Name':<25} {'Email':<30} {'City':<20}")
    print("=" * 80)
    
    for user in users:
        name = user['name'][:23] if len(user['name']) > 23 else user['name']
        email = user['email'][:28] if len(user['email']) > 28 else user['email']
        city = user['address']['city'][:18] if len(user['address']['city']) > 18 else user['address']['city']
        print(f"{user['id']:<5} {name:<25} {email:<30} {city:<20}")
    
    print("=" * 80)

def display_post_detail(post):
    """Display detailed information about a post."""
    print("\n" + "=" * 80)
    print(f"Post ID: {post['id']}")
    print(f"User ID: {post['userId']}")
    print(f"Title: {post['title']}")
    print(f"\nBody:\n{post['body']}")
    print("=" * 80)

def display_comments(comments):
    """Display comments in a formatted way."""
    print("\n" + "=" * 80)
    print("Comments:")
    print("=" * 80)
    
    for comment in comments:
        print(f"\nComment ID: {comment['id']}")
        print(f"Email: {comment['email']}")
        print(f"Name: {comment['name']}")
        print(f"Body: {comment['body'][:100]}...")
        print("-" * 80)

def main():
    """Main function to run the API integration script."""
    client = APIClient()
    
    print("=" * 80)
    print("API Integration - JSONPlaceholder Demo")
    print("=" * 80)
    
    while True:
        print("\nOptions:")
        print("1. View Posts")
        print("2. View Post Details")
        print("3. View Users")
        print("4. View Comments for a Post")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '5':
            print("\nThank you for using the API Integration script!")
            break
        
        try:
            if choice == '1':
                print("\nFetching posts...")
                posts = client.get_posts(limit=10)
                display_posts(posts)
            
            elif choice == '2':
                post_id = input("Enter post ID (1-100): ").strip()
                if not post_id.isdigit():
                    print("Error: Post ID must be a number")
                    continue
                print(f"\nFetching post {post_id}...")
                post = client.get_post(post_id)
                display_post_detail(post)
            
            elif choice == '3':
                print("\nFetching users...")
                users = client.get_users()
                display_users(users)
            
            elif choice == '4':
                post_id = input("Enter post ID (1-100): ").strip()
                if not post_id.isdigit():
                    print("Error: Post ID must be a number")
                    continue
                print(f"\nFetching comments for post {post_id}...")
                comments = client.get_comments(post_id=post_id)
                display_comments(comments)
            
            else:
                print("Invalid choice. Please select 1-5.")
        
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
