```python
book.title = "Nineteen Eighty-Four"
book.save()

# Check update
Book.objects.get(id=1).title
# Output: 'Nineteen Eighty-Four'
