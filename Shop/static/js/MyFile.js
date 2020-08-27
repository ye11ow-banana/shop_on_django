function click_on_btn_for_heart(id){
    btn = document.getElementById(id);
    btn.click();
}


let value_for_default = 1;


function cost_calculation(){
    let new_value = document.getElementById('value').value;
    let price = document.getElementById('price');
    if (value_for_default !== new_value){                          
        let result = new_value * (price.innerHTML/value_for_default);
        value_for_default = new_value;
        price.innerHTML = result; 
    }
}


document.querySelector('body').addEventListener('click', function(){
    cost_calculation();
});


var textarea = document.getElementsByClassName('textarea')[0];


if (textarea) {
    textarea.addEventListener('keyup', function(){
      if(this.scrollTop > 0){
        this.style.height = this.scrollHeight + "px";
      }
    });
}


let text_area = document.getElementsByClassName('text');
let sel = document.getElementsByClassName('product-details spad')[0];


for (let i = 0; i < text_area.length; i++) {
    if (text_area[i]) {
        sel.addEventListener('mouseover', function(){
            text_area[i].style.height = text_area[i].scrollHeight + "px";
        });   
    }            
}


let quantity_reviews = document.getElementById('quantity_reviews');


if (reviews.length) {
    quantity_reviews.innerHTML = '(' + reviews.length + ')';
}


function delete_review(id){

    let div_basket = document.getElementById('div_basket_' + id);
    let div_pencil = document.getElementById('div_pencil_' + id);
    let btn_basket = document.getElementById('btn_basket_' + id);
    let form_basket = document.getElementById('form_basket_' + id);

    div_basket.style.display = 'none';
    div_pencil.style.display = 'none';
    btn_basket.style.display = 'inline-block';
    form_basket.style.display = 'inline-block';
}


function edit_text(id){

    let div_basket = document.getElementById('div_basket_' + id);
    let div_pencil = document.getElementById('div_pencil_' + id);
    let btn_pencil = document.getElementById('btn_pencil_' + id);
    let button = document.getElementById('btn_pencil_form_' + id);
    let text_pencil = document.getElementById('text_pencil_' + id);

    div_basket.style.display = 'none';
    div_pencil.style.display = 'none';
    btn_pencil.style.display = 'inline-block';
    button.style.display = 'inline-block';
    text_pencil.readOnly = 0;
}


function back(id){

    let div_basket = document.getElementById('div_basket_' + id);
    let div_pencil = document.getElementById('div_pencil_' + id);
    let btn_pencil = document.getElementById('btn_pencil_' + id);
    let btn_basket = document.getElementById('btn_basket_' + id);
    let button = document.getElementById('btn_pencil_form_' + id);
    let form_basket = document.getElementById('form_basket_' + id);
    let text_pencil = document.getElementById('text_pencil_' + id);

    div_basket.style.display = 'inline-block';
    div_pencil.style.display = 'inline-block';
    btn_pencil.style.display = 'none';
    btn_basket.style.display = 'none';
    button.style.display = 'none';
    form_basket.style.display = 'none';
    text_pencil.readOnly = 1;
}


function show_answer_form(id){

    let answer_form = document.getElementById('answer_form_' + id);
    let answer_text = document.getElementById('answer_text_' + id);

    if (answer_form.style.display === 'none') {
        answer_form.style.display = 'inline-block';
        answer_text.focus();
    } else {
        answer_form.style.display = 'none';
    }
     
}


function show_answer(id){
    let answers = document.getElementsByClassName('answer_' + id);


    for (let i = 0; i < answers.length; i++) {
        if (answers[i].style.display === 'none') {
            answers[i].style.display = 'inline-block';
        } else {
            answers[i].style.display = 'none';
        }
        
    }
    
}


// -------------------------------------->


function make_str_from_list(args) {
    let str = '';
    for (let i = 0; i < args.length; i++) {
        str += '<div class="fa stars">' + args[i] + '</div>';
    }
    return str
}


function fill_in_missing_stars(args) {
    let result = [];

    let i = 0;
    while (i < 5) {
        if (typeof(args[i]) !== 'undefined') {
            
            result.push(args[i]);
        } else {
            result.push('<i class="fa fa-star-o" id="star_' + (i + 1) + '"></i>');
        }
        i++;
    } 

    return result
}

function create_list_of_full_stars(end) {
    let result = [];

    for (let i = 0; i < end; i++) {
        result.push('<i class="fa fa-star" id="star_' + (i + 1) + '"></i>');
    }

    return result
}


let default_str = document.getElementsByClassName('pochenu')[0].innerHTML;
let stars = document.getElementsByClassName('stars');
let main_star = document.getElementsByClassName('main_star')[0];


// function f4() {
//     for (let i = 0; i < stars.length; i++) {
//         stars[i].onmouseout = f1();
//         stars[i].onmouseover = f2();
//         stars[i].onclick = f3();
//     }
// }


// function f1() {
//     for (let i = 0; i < stars.length; i++) {
//         stars[i].addEventListener('mouseout', function() {       
//             document.getElementsByClassName('pochenu')[0].innerHTML = default_str;
//             f4();
//         });

//     }
// }

function f2() {
    for (let i = 0; i < stars.length; i++) {
        stars[i].addEventListener('mouseover', function() {       

            let index = stars[i].innerHTML[(stars[i].innerHTML).length - 7];
            let result = create_list_of_full_stars(index);
            let last_result = fill_in_missing_stars(result);
            main_star.innerHTML = make_str_from_list(last_result);
            f3();
            f2();
        });
    }
}

function f3() {
    for (let i = 0; i < stars.length; i++) {
        stars[i].addEventListener('click', function() {
            let input = document.getElementById('input_star');
            let button = document.getElementById('btn_star');

            input.value = stars[i].innerHTML[(stars[i].innerHTML).length - 7];
            button.click(); 
        });
    }
}

f3();
f2();