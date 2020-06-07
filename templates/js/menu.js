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
    if (itemsScrolled < 2) {
        prepend = true;
    }
    listOpts.items.forEach(function (ele) {
        ele.classList.remove('active');
    });
    if (itemsScrolled < listOpts.items.length) {
        listOpts.items[itemsScrolled].classList.add('active');
    }
    if(prepend) {
      var firstNode = listOpts.items[0];
      for (_x = itemsMax - 1; _x >= 0; _x--) {
            // if (window.CP.shouldStopExecution(1)) {
            //     break;
            // }
            var node = listOpts.items[_x];
            var newFirstNode = node;
            if (!cloned) {
                node = listOpts.items[_x].cloneNode(true);
            }
            scrollUl.insertBefore(node, firstNode)
            firstNode = newFirstNode;
        }
        this.scrollTop = this.scrollTop + listOpts.itemHeight * (itemsMax);
        initItems(true);
        cloned = true;
        itemsScrolled = 0;
    } else if (itemsScrolled > listOpts.items.length - 3) {
        for (_x = 0; _x <= itemsMax - 1; _x++) {
            // if (window.CP.shouldStopExecution(1)) {
            //     break;
            // }
            var node = listOpts.items[_x];
            if (!cloned) {
                node = listOpts.items[_x].cloneNode(true);
            }
            scrollUl.appendChild(node);
        }
        initItems(cloned);
        cloned = true;
        itemsScrolled = 0;
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
        var seamLessScrollPoint = (itemsMax - 3) * listOpts.itemHeight;
        scrollW.scrollTop = seamLessScrollPoint;
    }
}
document.addEventListener('DOMContentLoaded', function (event) {
    initItems(true, true);
    scrollW.onscroll = scrollWrap;
});