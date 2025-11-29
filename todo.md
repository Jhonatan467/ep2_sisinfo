# Categories Feature TODO

- [x] Create `Category` model with `name`, `slug`, optional `description`, and register in `blog/models.py`.
- [x] Connect `Post` to categories with a `ManyToManyField` and ensure migrations.
- [x] Generate and apply migrations for the new model and relationships.
- [x] Register `Category` in `blog/admin.py` with useful list filters/search.
- [x] Update forms/admin to manage categories when creating posts.
- [x] Add category navigation link(s) to `templates/base.html` and any shared layouts.
- [x] Implement category list and detail views in `blog/views.py`.
- [x] Wire new views in `blog/urls.py` and update `blog/templates` to reuse the post list for category filtering.
- [x] Update `post_detail.html` (and others) to display category badges linking to listings.
- [x] Write tests covering category model, views, and template integration.
- [x] Ensure templates handle posts without categories gracefully.
- [ ] Document feature in README/report and prepare deployment notes/screenshots.
- [x] Verify full test suite passes.
- [ ] Commit changes on `categories` branch and open PR for master.
