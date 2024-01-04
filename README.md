# 3615radio

A playlist from the #3615radio hashtag on the Fediverse

# How to use

1. Create a function in the Dev Tools that match https urls

```javascript
extractURLs = function extractURLs(text) {
  const regex = /(https?:\/\/[^\s]+)/g;
  const urls = text.match(regex);
  return urls;
}
```

2. Browse `https://mastovue.glitch.me/#/3615.computer/local/3615radio` then in the DevTools loop over `.media-content` class

```javascript
for (var i = 0; i < document.querySelectorAll(".media-content").length; i++) {
  console.log(
    extractURLs(document.querySelectorAll(".media-content")[i].textContent)[0]
  );
}
```

3. Right click > Save all messages in a file
5. Tidy up the file
6. Save as "playlist.m3u"
7. Et voilà
