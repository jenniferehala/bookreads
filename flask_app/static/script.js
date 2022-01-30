
// My Code for Google Search API //

function sendBookname() {
    var title = document.querySelector("#booktitle").value;
    getInfo(title);

}

async function getInfo(bookname) {
    var response = await fetch("https://www.googleapis.com/books/v1/volumes?q=" + bookname)
    var data = await response.json();
    console.log(data);
    createBook(data);
}

function createBook(data) {
    for (i = 0; i < data.items.length; i++) {
        document.querySelector("#books").innerHTML +=
            "<h5>" + data.items[i].volumeInfo.title + "</h5>" +
            "<h6>" + data.items[i].volumeInfo.description + "</h6>" +
            `<img src="${data.items[i].volumeInfo.imageLinks.smallThumbnail}"/>`;
    }
}

// Google Functions for API //

function onSignIn(googleUser) {
    console.log('User is' + JSON.stringify(googleUser.getBasicProfile()))
    document.querySelector('#content').innerText =
        googleUser.getBasicProfile().getName();
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}

// Sample JavaScript code for books.bookshelves.list
// See instructions for running APIs Explorer code samples locally:
// https://developers.google.com/explorer-help/guides/code_samples#javascript

function authenticate() {
    return gapi.auth2.getAuthInstance()
        .signIn({ scope: "https://www.googleapis.com/auth/books" })
        .then(function () { console.log("Sign-in successful"); },
            function (err) { console.error("Error signing in", err); });
}
function loadClient() {
    gapi.client.setApiKey("AIzaSyCOSj4RNxFodpNNgaf-hy_aHjCAtr9fTXM");
    return gapi.client.load("https://content.googleapis.com/discovery/v1/apis/books/v1/rest")
        .then(function () { console.log("GAPI client loaded for API"); },
            function (err) { console.error("Error loading GAPI client for API", err); });
}
// Make sure the client is loaded and sign-in is complete before calling this method.
function execute() {
    return gapi.client.books.bookshelves.list({
        "userId": "108743281303548137851"
    })
        .then(function (response) {
            // Handle the results here (response.result has the parsed body).
            console.log("Response", response);
            console.log(response.result)
        },
            function (err) { console.error("Execute error", err); });
}
gapi.load("client:auth2", function () {
    gapi.auth2.init({ client_id: "321302771227-4fuodheas35g5rsm2hoffvhkl1v4eeg0.apps.googleusercontent.com" });
});


// Google Default Viewer Google JS //

google.books.load();

        function initialize() {
            var viewer = new google.books.DefaultViewer(document.getElementById('viewerCanvas'));
            viewer.load('ISBN:0738531367');
        }

        google.books.setOnLoadCallback(initialize);