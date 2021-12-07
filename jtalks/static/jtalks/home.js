// code to load courses in home.html
$(document).ready(function() {
  //console.log('working')
  $('#load_more').on('click', function() {
    var _currentCourses = $('.product-box').length;
    var _limit = $(this).attr('data-limit')
    var _total = $(this).attr('data-total')
    // start ajax
    $.ajax({
      url: '/load-more-data/',
      data: {
        limit: _limit,
        offset: _currentCourses
      },
      dataType: 'json',
      beforeSend: function() {
        $('#load_more').attr('disabled', true);
        $('.load-more-icon').addClass('fa-spinner')
      },
      success: function(res) {
        $('.course-cards').append(res.data)
        $('#load_more').attr('disabled', false);
        $('.load-more-icon').removeClass('fa-spinner')
        
        if (_currentCourses == _total) {
          $('#load_more').remove();
          $('.product_end').show();
        }
      }
    })
    // end ajax
  })

  // load more products

  $('#load_more_products').on('click', function() {
    var _currentProducts = $('.card-box').length;
    var _limit = $(this).attr('data-limit')
    var _total = $(this).attr('data-total')

    // start ajax
    $.ajax({
      url: '/load_more_products/',
      data: {
        limit: _limit,
        offset: _currentProducts
      },
      dataType: 'json',
      beforeSend: function() {
        $('#load_more_products').attr('disabled', true);
        $('.load-more-icon').addClass('fa-spinner')
      },
      success: function(res) {
        $('.products-cards').append(res.data)
        $('#load_more_products').attr('disabled', false);
        $('.load-more-icon').removeClass('fa-spinner')
        
        if (_currentProducts == _total) {
          $('#load_more_products').remove();
          $('.end-products').show();
        }
      }
    })
    // end ajax
  })


  // add course review
  $('form#addForm').submit(function(e) {
    e.preventDefault()
    var _review = $('#id_review_text').val()
    var _rating = $('#id_review_rating option:selected').text();
    var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
    var course_id = $('input[name="course_id"]').val();

    $.ajax({
      url: '/course/save_review/',
      data: {
        'id': course_id,
        'review': _review,
        'rating': _rating,
        'csrfmiddlewaretoken': csrfmiddlewaretoken
      },
      dataType: 'json',
      success: function(data) {
        $('.modal').modal('hide');
        $('.hide_btn').hide();
        history.go(0);
      }
    })

  })

  // code to load reviews in course_detail.html
  $('#load_more_review').on('click', function() {
    var _currentReview = $('.review-box').length;
    var _limit = $(this).attr('data-limit')
    var _total = $(this).attr('data-total')
    var _course_id = $(this).attr('data-course-id')

    // start ajax
    $.ajax({
      url: '/course/load_more_review/',
      data: {
        limit: _limit,
        offset: _currentReview,
        id: _course_id
      },
      dataType: 'json',
      beforeSend: function() {
        $('#load_more_review').attr('disabled', true);
        $('.load-more-icon').addClass('fa-spinner')
      },
      success: function(res) {
        $('.review-list').append(res.data)
        $('#load_more_review').attr('disabled', false);
        $('.load-more-icon').removeClass('fa-spinner')

        if (_currentReview == _total) {
          $('#load_more_review').remove();
          $('.review_end').show();
        };
      }
    })
    // end ajax
  })

  // add to user library
  // this should be for payment first, not library
  $('#enroll_btn').on('click', function() {
    let _user = $(this).attr('data-user');
    let _id = $(this).attr('data-course-id');
    //console.log(_user, _id)

    $.ajax({
      url: '/course/add-to-library/',
      data: {
        'user': _user,
        'id': _id
      },
      dataType: 'json',
      beforeSend: function() {
        $('#enroll_btn').attr('disabled', true);
        $('.load-more-icon').addClass('fa-spinner')
      },
    })
  })

});