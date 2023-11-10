# thegoods > genurls

Create a urls.txt file containing a list of URLs extracted from the specified DOM element on the provided webpage, which can be identified by either its classes or its ID.

Using classes to find the DOM Element
```
python genurl.py https://example.com class "measure-long pad-left-400 pad-right-400 stack"
```

Using ID to find the DOM Element
```
python genurl.py https://example.com id "uniqueElementId"

```

A file named "url.txt" will be generated in the current directory.
