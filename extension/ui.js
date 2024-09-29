console.log('UI script loaded');

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'updateStatus') {
    console.log('received message: ', request.text);
    const obj = JSON.parse(request.text);
    document.getElementById('mainFactor').innerHTML = obj.total_score + '%';
    document.getElementById('tech').innerHTML = obj.aggregators.tech_standards.score + '%';
    document.getElementById('tech_description').innerHTML = obj.aggregators.tech_standards.notes.join('</br>');
    document.getElementById('review').innerHTML = obj.aggregators.reviews.score + '%';
    document.getElementById('review_description').innerHTML = obj.aggregators.reviews.notes.join('</br>');
    document.getElementById('phising').innerHTML = obj.aggregators.phishing.score + '%';
    document.getElementById('phising_description').innerHTML = obj.aggregators.phishing.notes.join('</br>');
    document.getElementById('social').innerHTML = obj.aggregators.social.score + '%';
    document.getElementById('social_description').innerHTML = obj.aggregators.social.notes.join('</br>');
  }
});
