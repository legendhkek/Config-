# Documentation Instructions

**Apply To**: `*.md`, `README.md`, documentation files

## Documentation Style Guide

### General Principles

- **Clarity**: Write in clear, concise language that is easy to understand
- **Completeness**: Include all necessary information for users to successfully use the configurations
- **Consistency**: Match the existing documentation style and formatting
- **Accuracy**: Ensure all technical details, version numbers, and examples are correct
- **Maintainability**: Structure documentation so it's easy to update when code changes

## README.md Structure

The main README follows this structure:

1. **Repository Overview**: Brief description of the repository's purpose
2. **Available Configurations**: List of all configurations with details
3. **Configuration Details**: Specific information for each configuration
4. **Usage Instructions**: How to use the configurations
5. **Support & Updates**: Contact and repository information
6. **Changelog**: Version history and updates

### Adding New Configuration Section

When adding a new configuration, use this template:

```markdown
### [Number]. [Icon] [Service Name] - [Feature Description] (NEW!)
**File:** `SERVICE.COM.loli` or `service.com.opk`
**Version:** 1.0.0
**Category:** [Category Name]
**Created:** YYYY-MM-DD

[Brief description of what the configuration does]:
- **CPM**: [Number] checks per minute
- **Bots**: [Number] concurrent workers
- **Method**: [API/Browser description]
- **Data Capture**: [Comma-separated list of captured fields]
- **Format**: LoliCode/LoliScript or OPK

**Features:**
- [Feature 1]
- [Feature 2]
- [Feature 3]
- [Feature 4]

**Advanced Features (if applicable):**
- [Advanced feature 1]
- [Advanced feature 2]

**Documentation:**
- 📖 [Usage Guide](SERVICE_USAGE_GUIDE.md) - Step-by-step setup
- 📋 [Technical Specifications](SERVICE_TECHNICAL_SPECS.md) - Detailed documentation
```

## Service-Specific Documentation Files

### Usage Guide (SERVICE_USAGE_GUIDE.md)

Create a dedicated usage guide for each major configuration:

**Structure:**
1. **Overview**: What the configuration does and who it's for
2. **Prerequisites**: Required software, accounts, and resources
3. **Quick Start**: Minimal steps to get up and running
4. **Detailed Setup**: Step-by-step instructions with screenshots
5. **Configuration Options**: All available settings and their effects
6. **Troubleshooting**: Common issues and solutions
7. **Best Practices**: Tips for optimal performance
8. **Examples**: Real-world usage scenarios

**Template:**
```markdown
# [Service Name] - Usage Guide

## Overview
[What this configuration does and its main use cases]

## Prerequisites
- OpenBullet 2 (version X.X or later)
- [Any accounts or API keys needed]
- [Proxy requirements]
- [Other dependencies]

## Quick Start

### 1. Installation
[Steps to install/import the configuration]

### 2. Basic Configuration
[Minimal settings to get started]

### 3. Running Your First Check
[Simple example with sample data]

## Detailed Setup

### Input Format
[Expected format for credentials/data]
```
example:format
```

### Proxy Configuration
[Proxy types supported and how to configure them]

### [Other sections as needed]

## Configuration Options

### Basic Settings
- **CPM**: [Description and recommended values]
- **Bots**: [Description and recommended values]
- **Timeout**: [Description]

### Advanced Settings
- **[Setting Name]**: [Description]

## Troubleshooting

### [Common Issue 1]
**Problem**: [Description]
**Solution**: [Steps to resolve]

### [Common Issue 2]
**Problem**: [Description]
**Solution**: [Steps to resolve]

## Best Practices
- [Tip 1]
- [Tip 2]
- [Tip 3]

## Examples

### Example 1: [Scenario]
[Detailed example with commands/settings]

### Example 2: [Scenario]
[Detailed example with commands/settings]
```

### Technical Specifications (SERVICE_TECHNICAL_SPECS.md)

Create detailed technical documentation:

**Structure:**
1. **Technical Overview**: Architecture and design decisions
2. **API Endpoints**: All endpoints used with request/response examples
3. **Authentication Flow**: Step-by-step authentication process
4. **Data Structures**: JSON schemas and data formats
5. **Error Codes**: All possible errors and handling
6. **Performance Metrics**: CPM, threading, and optimization details
7. **Security Features**: Anti-bot evasion, TLS settings, etc.
8. **Configuration Schema**: Complete configuration structure

**Template:**
```markdown
# [Service Name] - Technical Specifications

## Technical Overview

### Architecture
[Description of how the configuration works]

### Design Decisions
[Why certain approaches were chosen]

## API Endpoints

### 1. [Endpoint Name]
**URL**: `https://api.service.com/endpoint`
**Method**: GET/POST
**Headers**:
```http
Header-Name: value
```

**Request Body** (if applicable):
```json
{
  "key": "value"
}
```

**Response** (success):
```json
{
  "success": true,
  "data": {}
}
```

**Response** (error):
```json
{
  "error": "error message"
}
```

### 2. [Another Endpoint]
[Same structure]

## Authentication Flow

### Step 1: [Step Name]
[Description with request/response]

### Step 2: [Step Name]
[Description with request/response]

## Data Structures

### [Structure Name]
```json
{
  "field": "type - description"
}
```

## Error Codes

| Code | Message | Handling |
|------|---------|----------|
| 401 | Unauthorized | Mark as FAIL |
| 429 | Rate Limited | RETRY with backoff |
| [etc] | [etc] | [etc] |

## Performance Metrics

### Speed
- **CPM**: [Number] checks per minute
- **Bots**: [Number] concurrent workers
- **Avg Response Time**: [Time]

### Threading Configuration
- [Details about threading]

### Optimization Techniques
- [Optimization 1]
- [Optimization 2]

## Security Features

### Anti-Bot Evasion
- [Feature 1]
- [Feature 2]

### TLS Configuration
- **Version**: TLS 1.3
- **Cipher Suites**: [List]
- [Other TLS details]

## Configuration Schema

### LoliCode Structure
```loli
[Configuration structure]
```

### OPK Structure (if applicable)
```json
{
  "configuration": "structure"
}
```
```

## Markdown Formatting Standards

### Headers

Use ATX-style headers (# syntax):

```markdown
# H1 - Main Title
## H2 - Major Section
### H3 - Subsection
#### H4 - Detail Section
```

### Lists

**Unordered lists** (use - consistently):
```markdown
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3
```

**Ordered lists**:
```markdown
1. First step
2. Second step
3. Third step
```

### Code Blocks

Always specify language for syntax highlighting:

````markdown
```python
# Python code
def function():
    pass
```

```bash
# Bash commands
npm install
```

```json
{
  "key": "value"
}
```
````

### Links

Use descriptive link text:
```markdown
See [Installation Guide](INSTALL.md) for setup instructions.
[OpenBullet 2](https://github.com/openbullet/OpenBullet2) is required.
```

### Tables

Use tables for structured data:
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

### Emphasis

- **Bold** for important terms: `**bold**`
- *Italic* for emphasis: `*italic*`
- `Code` for inline code/commands: `` `code` ``

### Blockquotes

Use for important notes or tips:
```markdown
> **Note**: This is an important note for users.

> **Warning**: This action cannot be undone.

> **Tip**: Use high-quality proxies for best results.
```

## Emojis and Icons

Use emojis consistently for visual markers:

- 🎯 Repository/Project info
- 📦 Packages/Files
- 🔐 Security/Authentication
- 🚀 Performance/Speed
- 🔒 Security features
- 🔄 Updates/Changes
- 🌐 Network/Proxy
- 🧵 Threading/Concurrency
- 📊 Data/Metrics
- 📈 Analytics/Reports
- 💾 Storage/Cache
- 📝 Logs/Documentation
- 🎯 Goals/Objectives
- 🛡️ Protection/Defense
- ✅ Success/Enabled
- ❌ Failure/Disabled
- ⚠️ Warning/Caution
- 💡 Tip/Suggestion
- 🔧 Configuration/Settings
- 📖 Documentation
- 📋 Specifications
- 🤖 Bot/Automation
- ✈️ Airlines category
- 🔐 Cryptocurrency category
- 📺 Streaming category
- ✨ New features

## Version Information

Always include version numbers in documentation:

```markdown
**Version:** 2.1.0
**Last Updated:** 2025-11-20
**Author:** legendhkek
```

Update versions when making changes:
- **Major version (X.0.0)**: Breaking changes or complete rewrites
- **Minor version (0.X.0)**: New features or significant improvements
- **Patch version (0.0.X)**: Bug fixes or minor tweaks

## Changelog Format

Maintain a clear changelog:

```markdown
## Changelog

### Version 2.1.0 (2025-11-20)
- **NEW: [Feature Name]**
  - Description of new feature
  - Sub-feature details
- **IMPROVED: [Feature Name]**
  - Description of improvement
- **FIXED: [Bug Name]**
  - Description of fix

### Version 2.0.0 (2025-11-19)
- Complete rewrite with [major changes]
- [List of major changes]

### Version 1.0.0 (2025-11-18)
- Initial release
- [Initial features]
```

## Examples and Code Samples

### Provide Working Examples

Always include complete, working examples:

```markdown
### Example: Checking Accounts with Proxies

**Input file** (`combos.txt`):
```
user1@example.com:password123
user2@example.com:securepass456
```

**Proxy file** (`proxies.txt`):
```
123.45.67.89:8080
98.76.54.32:3128
```

**Configuration**:
1. Load `SERVICE.COM.loli` in OpenBullet 2
2. Import combos from `combos.txt`
3. Import proxies from `proxies.txt`
4. Set Bots to 100
5. Start the job

**Expected Results**:
- Valid accounts: Marked as SUCCESS with captured data
- Invalid credentials: Marked as FAIL
- Rate limited: Marked as RETRY
```

## Troubleshooting Section Format

Structure troubleshooting sections consistently:

```markdown
## Troubleshooting

### Issue: [Problem Description]

**Symptoms:**
- [Symptom 1]
- [Symptom 2]

**Possible Causes:**
- [Cause 1]
- [Cause 2]

**Solutions:**

1. **[Solution Name]**
   ```bash
   # Commands or steps
   ```
   Expected result: [What should happen]

2. **[Alternative Solution]**
   [Steps]

**Still Having Issues?**
- [Additional help resources]
- [Contact information]
```

## Best Practices

1. **Update Documentation with Code**: When code changes, update documentation immediately
2. **Keep Examples Current**: Test examples to ensure they still work
3. **Link Related Docs**: Cross-reference related documentation
4. **Use Consistent Terminology**: Use the same terms throughout all docs
5. **Include Prerequisites**: Always list what users need before starting
6. **Provide Context**: Explain why, not just how
7. **Test Instructions**: Follow your own instructions to verify they work
8. **Version Control**: Document what version of software is required
9. **Date Updates**: Include dates on all documentation updates
10. **Accessibility**: Write for users with varying technical backgrounds

## Notes for Copilot

- Match the existing documentation style exactly
- Preserve formatting, emojis, and structure
- Update version numbers when making changes
- Keep technical accuracy as the highest priority
- Include practical examples for all features
- Cross-reference related documentation files
- Test that all links work before committing
