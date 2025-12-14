# API Integration

A Python script that interacts with an external API to fetch and display data. This project uses the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/), a free fake REST API for testing and prototyping.

## Features

- Fetch and display a list of posts
- View detailed information about a specific post
- Fetch and display user information
- View comments for a specific post
- Interactive command-line interface
- Error handling for network and API issues
- No external dependencies (uses Python standard library)

## Requirements

- Python 3.6 or higher
- Internet connection (to access the API)

## API Used

This script uses the JSONPlaceholder API, which provides fake data for:
- Posts
- Comments
- Users
- Albums
- Photos
- Todos

## Usage

1. Navigate to the api_integration directory:
   ```bash
   cd api_integration
   ```

2. Run the script:
   ```bash
   python api_client.py
   ```

3. Follow the on-screen prompts:
   - Select an option (1-5)
   - View different types of data from the API
   - Exit when done (option 5)

## Example Output

### Viewing Posts
```
================================================================================
ID    User ID    Title                                                        
================================================================================
1     1          sunt aut facere repellat provident occaecati excepturi op...
2     1          qui est esse...
3     1          ea molestias quasi exercitationem repellat qui ipsa sit ...
...
```

### Viewing Users
```
================================================================================
ID    Name                      Email                          City                
================================================================================
1     Leanne Graham             Sincere@april.biz              Gwenborough         
2     Ervin Howell              Shanna@melissa.tv              Wisokyburgh         
...
```

### Viewing Post Details
```
================================================================================
Post ID: 1
User ID: 1
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit

Body:
quia et suscipit
suscipit recusandae consequuntur expedita et cum
reprehenderit molestiae ut ut quas totam
nostrum rerum est autem sunt rem eveniet architecto
================================================================================
```

## Error Handling

- Network errors: The script will display an error message if it cannot connect to the API
- Invalid input: Non-numeric inputs for IDs will be caught and an error message will be displayed
- API errors: If the API returns an error status code, it will be displayed to the user
- Timeout: Requests will timeout after 10 seconds

## Customization

You can modify the `APIClient` class to:
- Change the API endpoint (update `BASE_URL`)
- Add more API methods
- Adjust the timeout value
- Change the display format
