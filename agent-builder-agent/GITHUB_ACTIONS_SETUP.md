# GitHub Actions Setup Guide

This guide will help you set up the Agent Builder to run automatically every day using GitHub Actions, even when your PC is offline.

## Why GitHub Actions?

- ✅ Runs in the cloud (no need for your PC to be on)
- ✅ Free for public repositories
- ✅ Reliable scheduling
- ✅ Automatic git commits and pushes
- ✅ Email notifications on completion

## Setup Steps

### 1. Create the Workflow File

The workflow file is already created at `.github/workflows/daily-agent-builder.yml`. It's configured to run daily at 9:00 AM UTC.

### 2. Configure GitHub Secrets

You need to add secrets to your GitHub repository for the Agent Builder to work:

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** for each of the following:

#### Required Secrets:

- **`OPENAI_API_KEY`**: Your OpenAI API key
- **`SMTP_USER`**: Your Gmail address (for sending emails)
- **`SMTP_PASSWORD`**: Your Gmail app password (not your regular password)
- **`EMAIL_RECIPIENT`**: Email address to receive reports

#### Optional Secrets (with defaults):

- **`OPENAI_MODEL`**: Model to use (default: `gpt-4o`)
- **`SMTP_SERVER`**: SMTP server (default: `smtp.gmail.com`)
- **`SMTP_PORT`**: SMTP port (default: `587`)
- **`GITHUB_REPO_URL`**: Your repository URL (auto-detected if not set)
- **`DAILY_RUN_TIME`**: Run time (default: `09:00`)
- **`GIT_AUTHOR_NAME`**: Name for git commits (default: `Agent Builder`)
- **`GIT_AUTHOR_EMAIL`**: Email for git commits (default: `agent-builder@noreply.github.com`)

### 3. Adjust Schedule (Optional)

To change when the agent runs, edit `.github/workflows/daily-agent-builder.yml`:

```yaml
schedule:
  - cron: '0 9 * * *'  # 9:00 AM UTC daily
```

Cron format: `minute hour day month day-of-week`

Examples:
- `'0 9 * * *'` - 9:00 AM UTC daily
- `'0 14 * * *'` - 2:00 PM UTC daily (9:00 AM EST)
- `'0 17 * * *'` - 5:00 PM UTC daily (12:00 PM PST)

**Note**: GitHub Actions uses UTC time. Convert your local time to UTC.

### 4. Test the Workflow

1. Go to **Actions** tab in your GitHub repository
2. Click **Daily Agent Builder** workflow
3. Click **Run workflow** → **Run workflow** (manual trigger)
4. Watch it run and check the logs

### 5. Verify It Works

After the workflow runs:
- Check the **Actions** tab for run status
- Check your repository for new agent directories in `ai-built-agents/`
- Check your email for the report (if configured)
- Check the updated README files

## Troubleshooting

### Workflow Not Running

- Check that the workflow file is in `.github/workflows/` directory
- Verify the cron schedule syntax is correct
- Check GitHub Actions is enabled for your repository (Settings → Actions)

### Authentication Errors

- Verify `OPENAI_API_KEY` secret is set correctly
- Check that the API key has sufficient credits

### Email Not Sending

- Verify `SMTP_USER`, `SMTP_PASSWORD`, and `EMAIL_RECIPIENT` are set
- Check that you're using a Gmail app password (not regular password)
- Check workflow logs for email errors

### Git Push Fails

- Ensure the workflow has write permissions:
  - Go to Settings → Actions → General
  - Under "Workflow permissions", select "Read and write permissions"
  - Check "Allow GitHub Actions to create and approve pull requests"

### Workflow Runs But No Agent Created

- Check the workflow logs for errors
- Verify all required secrets are set
- Check that the OpenAI API key has sufficient credits

## Manual Trigger

You can manually trigger the workflow anytime:
1. Go to **Actions** tab
2. Click **Daily Agent Builder**
3. Click **Run workflow** button

## Monitoring

- View workflow runs in the **Actions** tab
- Each run shows logs, duration, and status
- Failed runs will show error details
- Email reports (if configured) will include success/failure status

## Cost Considerations

- **GitHub Actions**: Free for public repos (2000 minutes/month)
- **OpenAI API**: Pay per use (varies by model)
- Each agent build typically uses 1-3 API calls

## Alternative: Cloud Server

If you prefer running on a cloud server instead:

1. Set up a VPS (DigitalOcean, AWS EC2, etc.)
2. Install Python and dependencies
3. Set up a cron job:
   ```bash
   # Edit crontab
   crontab -e
   
   # Add this line (runs daily at 9 AM)
   0 9 * * * cd /path/to/agent-builder-agent && /usr/bin/python3 main.py --schedule
   ```

GitHub Actions is recommended for simplicity and reliability.

