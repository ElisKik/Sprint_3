function isScrolledIntoView(element) {
    var rect = element.getBoundingClientRect();
    var isVisible = (rect.top >= 0) && (rect.bottom <= window.innerHeight);

    return isVisible;
}
