;(function($, window, document, undefined) {

    var previousScroll = 0, // previous scroll position
        menuOffset = 54, // height of menu (once scroll passed it, menu is hidden)
        detachPoint = 650, // point of detach (after scroll passed it, menu is fixed)
        hideShowOffset = 6; // scrolling value after which triggers hide/show menu
    // on scroll hide/show menu
    $(window).scroll(function() {
      if (!$('nav').hasClass('expanded')) {
        var currentScroll = $(this).scrollTop(), // gets current scroll position
            scrollDifference = Math.abs(currentScroll - previousScroll); // calculates how fast user is scrolling
        // if scrolled past menu
        if (currentScroll > menuOffset) {
          // if scrolled past detach point add class to fix menu
          if (currentScroll > detachPoint) {
            if (!$('nav').hasClass('detached'))
              $('nav').addClass('detached');
          }
          // if scrolling faster than hideShowOffset hide/show menu
          if (scrollDifference >= hideShowOffset) {
            if (currentScroll > previousScroll) {
              // scrolling down; hide menu
              if (!$('nav').hasClass('invisible'))
                $('nav').addClass('invisible');
            } else {
              // scrolling up; show menu
              if ($('nav').hasClass('invisible'))
                $('nav').removeClass('invisible');
            }
          }
        } else {
          // only remove “detached” class if user is at the top of document (menu jump fix)
          if (currentScroll <= 0){
            $('nav').removeClass();
          }
        }
        // if user is at the bottom of document show menu
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
          $('nav').removeClass('invisible');
        }
        // replace previous scroll position with new one
        previousScroll = currentScroll;
      }
    })
    


  })(jQuery, window, document);