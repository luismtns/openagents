# openagents rules (generate)

Step 3 of `openagents rules` -- write three files to `.agents/rules/`.
Every rule must be **generic** (pattern, not path), **positive**, and
**verifiable**.

### conventions.md
```markdown
# conventions
## Principles
<why these conventions exist -- clarity, consistency, type safety>
## Naming
- <pattern>: <description>
## Imports and exports
- <project-specific import style>
## Linting and formatting
- <linter config summary>
## Testing
- <test runner, naming, location>
```

### architecture.md
```markdown
# architecture
## Directory layout
```
<project tree summary, max depth 3>
<!-- NOTE: structure at time of generation; new dirs follow the same split. -->
```
## Module responsibilities
- <directory>: <what belongs here>
## Boundaries
- <what crosses boundaries and how>
```

### generation.md
```markdown
# generation
When creating a new <X>, follow the pattern in <existing file>:
1. Create file under the same domain/layer pattern
2. Use the same export style as <similar file>
3. Follow the same error handling / state / API patterns
4. Add tests following the same structure
## Cross-cutting concerns
- <shared patterns: logging, error handling, validation, auth>
```