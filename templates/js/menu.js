var scrollW = document.getElementById('wrap-scroll');
var scrollUl = document.getElementById('ul-scroll');
var itemsScrolled, itemsMax, cloned = false;
var listOpts = {
    itemCount: null,
    itemHeight: null,
    items: []
};
function scrollWrap() {
    itemsScrolled = Math.ceil((this.scrollTop + listOpts.itemHeight / 2) / listOpts.itemHeight);
    prepend = false;
    if (this.scrollTop < 1) {
        itemsScrolled = 0;
    }
    listOpts.items.forEach(function (ele) {
        ele.classList.remove('active');
    });
    if (itemsScrolled < listOpts.items.length) {
        listOpts.items[itemsScrolled].classList.add('active');
    }
    if(itemsScrolled < listOpts.items.length/3) {
        this.scrollTop = this.scrollTop + (listOpts.itemCount/3 * listOpts.itemHeight)
        console.log("Too low. Changed from " + this.scrollTop + " to " + this.scrollTop + (listOpts.itemCount * listOpts.itemHeight))
    } else if (itemsScrolled > 2*listOpts.items.length/3) {
        this.scrollTop = this.scrollTop - (listOpts.itemCount/3 * listOpts.itemHeight)
        console.log("Too high. Changed from " + this.scrollTop + " to " + this.scrollTop - (listOpts.itemCount * listOpts.itemHeight))
    }
}
function initItems(scrollSmooth, init) {
    listOpts.items = [].slice.call(scrollUl.querySelectorAll('li'));
    listOpts.itemHeight = listOpts.items[0].clientHeight;
    listOpts.itemCount = listOpts.items.length;
    if (!itemsMax) {
        itemsMax = listOpts.itemCount;
    }
    if (scrollSmooth && init) {
        console.log("YOOO")
        var seamLessScrollPoint = (itemsMax - 4) * listOpts.itemHeight;
        scrollW.scrollTop = seamLessScrollPoint;
    }
}
document.addEventListener('DOMContentLoaded', function (event) {
    initItems(true, true);
    scrollW.onscroll = scrollWrap;
});