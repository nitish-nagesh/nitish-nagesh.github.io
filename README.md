# Nitish Nagesh - Academic Website

This is my personal academic website built with Jekyll. It showcases my research, experience, publications, and achievements.

## Features

- **Modern Design**: Clean, responsive design with smooth scrolling navigation
- **Academic Focus**: Structured sections for education, experience, publications, and awards
- **SEO Optimized**: Built-in SEO tags and meta descriptions
- **Mobile Friendly**: Responsive design that works on all devices
- **Fast Loading**: Optimized CSS and JavaScript

## Local Development

To run this site locally:

1. **Install Ruby and Jekyll** (if not already installed):
   ```bash
   # On macOS with Homebrew
   brew install ruby
   gem install jekyll bundler
   ```

2. **Install dependencies**:
   ```bash
   bundle install
   ```

3. **Run the development server**:
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**: Open http://localhost:4000 in your browser

## File Structure

```
├── _config.yml          # Site configuration
├── _layouts/            # Jekyll layouts
│   └── default.html     # Main layout template
├── assets/              # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   ├── img/            # Images
│   └── pdf/            # PDF files (CV, etc.)
├── _people/            # People collection (for team members)
├── _projects/          # Projects collection
├── _posts/             # Blog posts
├── _talks/             # Talks/presentations
└── index.md            # Home page content
```

## Customization

### Site Configuration (`_config.yml`)

Update the following fields in `_config.yml`:

- `title`: Your name
- `description`: Your tagline
- `email`: Your email address
- `github`, `linkedin`, `twitter`: Your social media handles
- `avatar`: Path to your profile picture
- `cv`: Path to your CV PDF

### Adding Content

1. **Blog Posts**: Add markdown files to `_posts/` with YAML front matter
2. **Projects**: Add project files to `_projects/` collection
3. **Talks**: Add presentation files to `_talks/` collection
4. **Team Members**: Add people files to `_people/` collection

### Styling

The main stylesheet is in `assets/css/main.css`. The design uses CSS custom properties for easy theming:

- `--bg`: Background color
- `--text`: Text color
- `--accent`: Primary accent color
- `--accent-hover`: Hover state color

## Deployment

This site is configured for GitHub Pages. Simply push your changes to the main branch and GitHub Pages will automatically build and deploy your site.

## License

This project is open source and available under the [MIT License](LICENSE).

## Credits

- Built with [Jekyll](https://jekyllrb.com/)
- Styled with modern CSS
- Icons from [Favicon Farm](https://fav.farm/) # Force rebuild
