// console.log(site_settings)
$(document).ready(function() {
    // our story section
    let aboutUs = site_settings.about_us;
    let ourStoryBody = $("#ourStoryBody");
    let ourStoryParagraphs = aboutUs.our_story.text.paragraphs;

    $("#ourStoryTitle").text(aboutUs.our_story.title);

    // fill our story body paragraphs
    for (let p of ourStoryParagraphs){
        let paragraphElem = `<p class="stext-113 cl6 p-b-26">${p}</p>`;
        ourStoryBody.append(paragraphElem);

    }
    // set image of our story
    $("#ourStoryPic").attr("src", aboutUs.our_story.pic_url)

    // our mission section
    let ourMissionBody = $("#ourMissionBody");
    let ourMissionParagraphs = aboutUs.our_mission.text.paragraphs;
    let ourMissionQuotations = aboutUs.our_mission.text.quotations;
    $("#ourMissionTitle").text(aboutUs.our_mission.title);

    // fill our mission body paragraphs
    for (let p of ourMissionParagraphs){
        let paragraphElem = `<p class="stext-113 cl6 p-b-26">${p}</p>`;
        ourMissionBody.append(paragraphElem);

    }

    // fill our Mission Quotations
    for (let elem of ourMissionQuotations){
        let p = `<p class="stext-114 cl6 p-r-40 p-b-11">${elem.quote}</p>`;
        let span = `<span className="stext-111 cl8">${elem.narrator}</span>`
        $("#ourMissionQuotations").append(p, span);

    }

    // set image of our mission
    $("#ourMissionPic").attr("src", aboutUs.our_mission.pic_url)
    // core/images/about_page/about2.jpg
});

