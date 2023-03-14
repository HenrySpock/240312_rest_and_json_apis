console.log('checking in') 

function getCupcakes() {
  axios.get('/api/cupcakes')
    .then(function(response) {
    let cupcakes = response.data.cupcakes;

    for (let i = 0; i < cupcakes.length; i++) {
        let li = document.createElement('li');
        li.textContent = cupcakes[i].flavor + ': ' + cupcakes[i].rating;

        // create an image element and set its source attribute to the image URL
        let img = document.createElement('img');
        img.src = cupcakes[i].image;

        // append the image element to the list item
        li.appendChild(img);

        document.querySelector('#cupcakes-list').appendChild(li);
    }
    })
    .catch(function(error) {
    console.log(error);
    });
}
  

// function addCupcake(event) {
// event.preventDefault();
// let form = document.querySelector('#new-cupcake-form');
// let flavor = form.querySelector('#flavor').value;
// let size = form.querySelector('#size').value;
// let rating = form.querySelector('#rating').value;
// let image = form.querySelector('#image').value;

// axios.post('/api/cupcakes', {
//     flavor: flavor,
//     size: size,
//     rating: rating,
//     image: image
// })
//     .then(function(response) {
//     let cupcake = response.data.cupcake;
//     let li = document.createElement('li');
//     li.textContent = cupcake.flavor + ': ' + cupcake.rating; 
//     document.querySelector('#cupcakes-list').appendChild(li);
//     })
//     .catch(function(error) {
//     console.log(error);
//     });
// }

function addCupcake(event) {
    event.preventDefault();
    let form = document.querySelector('#new-cupcake-form');
    let flavor = form.querySelector('#flavor').value;
    let size = form.querySelector('#size').value;
    let rating = form.querySelector('#rating').value;
    let image = form.querySelector('#image').value;

    axios.post('/api/cupcakes', {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image
    })
        .then(function(response) {
            let cupcake = response.data.cupcake;
            let li = document.createElement('li');
            li.textContent = cupcake.flavor + ': ' + cupcake.rating;            
            // create an image element and set its source attribute to the image URL
            let img = document.createElement('img');
            img.src = cupcake.image; 
            console.log('hello')
            // append the image element to the list item
            li.appendChild(img);

            document.querySelector('#cupcakes-list').appendChild(li);
        })
        .catch(function(error) {
            console.log(error);
        });
}



getCupcakes();
let form = document.querySelector('#new-cupcake-form');
form.addEventListener('submit', addCupcake);