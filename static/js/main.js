document.addEventListener('DOMContentLoaded', function () {
    M.AutoInit();
    M.Dropdown.init(document.querySelectorAll('.dropdown-trigger'), {
        constrainWidth: false,
        coverTrigger: false
    });
});