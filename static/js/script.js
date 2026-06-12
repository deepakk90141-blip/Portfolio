const homeContainer = document.querySelector('.main_head');
const caseContainer = document.querySelector('.case-study-page-container');
const targets = document.querySelectorAll('.case-study-page-container .content, .case-study-page-container .case-study-item');

function hideAll() {
    targets.forEach(section => {
        section.style.display = 'none';
    });
    if (caseContainer) {
        caseContainer.style.display = 'none';
    }
}

function showHome() {
    hideAll();
    if (homeContainer) {
        homeContainer.style.display = '';
    }
}

function showTargets(targetIds, replaceState = false) {
    if (!Array.isArray(targetIds)) {
        targetIds = targetIds.split(',').map(id => id.trim()).filter(Boolean);
    }

    if (targetIds.length === 0) {
        return;
    }

    hideAll();

    if (homeContainer) {
        homeContainer.style.display = 'none';
    }
    if (caseContainer) {
        caseContainer.style.display = '';
    }

    const shownIds = [];

    targetIds.forEach(id => {
        const section = document.getElementById(id);
        if (section) {
            section.style.display = 'block';
            shownIds.push(id);
        }
    });

    if (shownIds.length === 0) {
        showHome();
        return;
    }

    const stateValue = shownIds.join(',');
    const urlHash = `#${shownIds[shownIds.length - 1]}`;

    if (replaceState) {
        history.replaceState({ section: stateValue }, '', `${location.pathname}${urlHash}`);
    } else {
        history.pushState({ section: stateValue }, '', `${location.pathname}${urlHash}`);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    history.replaceState({ section: 'home' }, '', location.pathname);

    document.querySelectorAll('.open-section').forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            const target = button.dataset.target;
            if (target) {
                showTargets(target);
            }
        });
    });

    if (window.location.hash) {
        const hashTarget = window.location.hash.substring(1);
        if (hashTarget) {
            showTargets(hashTarget, true);
        }
    }
});

window.addEventListener('popstate', event => {
    if (event.state && event.state.section === 'home') {
        showHome();
    } else if (event.state && event.state.section) {
        showTargets(event.state.section, true);
    } else {
        showHome();
    }
});