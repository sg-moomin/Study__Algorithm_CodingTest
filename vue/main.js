
  var app = new Vue({
    // vue는 reactive함
    el : '#app', // instance -> div id와 연동시켜줌
    data: {
      Product: 'hello',
      inStock: true,
      inventory: 100
    }
  });


  var app2 = new Vue({
    el: '#app-2',
    data: {
      Product: '이 페이지는 ' + new Date() + ' 에 로드 되었습니다'
    }
  });

  var app3 = new Vue({
    el: '#app-3',
    data: {
      seen : true
    }
  });

  var app4 = new Vue({
    el: '#app-4',
    data: {
      todos: [
        { text: 'JavaScript 배우기' },
        { text: 'Vue 배우기' },
        { text: '무언가 멋진 것을 만들기' }
      ]
    }
  });
