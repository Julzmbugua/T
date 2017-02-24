var  mn = $(".nav");
                mns = "main-nav-scrolled";
                hdr = $('.carousel slide').height();

              $(window).scroll(function() {
                if( $(this).scrollTop() > hdr ) {
                  mn.addClass(mns);
                } else {
                  mn.removeClass(mns);
                }
              });