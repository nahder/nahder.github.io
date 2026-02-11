# Running the site locally

## One-time setup

### 1. Install Ruby and Bundler

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y ruby-full ruby-bundler
```

**macOS:** Ruby is usually pre-installed. Install Bundler if needed: `gem install bundler`

**Alternative (any OS):** [rbenv](https://github.com/rbenv/rbenv) or [asdf](https://asdf-vm.com/) to manage Ruby versions.

### 2. Install gems

From the project root:

```bash
bundle install
```

## Run the site

Start the Jekyll server:

```bash
bundle exec jekyll serve --livereload
```

Or use the helper script:

```bash
./bin/serve
```

Then open **http://localhost:4000** in your browser. With `--livereload`, the page refreshes when you edit content.

To listen on all interfaces (e.g. from another device):  
`bundle exec jekyll serve --livereload --host 0.0.0.0`
