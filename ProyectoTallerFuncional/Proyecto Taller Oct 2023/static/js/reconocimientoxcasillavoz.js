$(document).ready(function() {
    var recognition1 = new webkitSpeechRecognition();
    recognition1.continuous = true;
    recognition1.lang = "es";
 
    $('#search_input1').click(function(event) {
        recognition1.start();
    });
 
    recognition1.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input1').val(finalResult);
            }
        }
    };
});
var recognition1 = new webkitSpeechRecognition();
recognition1.continuous = true;
recognition1.lang = "es";
$('#search_input1').click(function(event) {
    recognition1.start();
});
recognition1.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input1').val(finalResult);
        }
    }
};

//input2
$(document).ready(function() {
    var recognition2 = new webkitSpeechRecognition();
    recognition2.continuous = true;
    recognition2.lang = "es";
 
    $('#search_input2').click(function(event) {
        recognition2.start();
    });
 
    recognition2.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input2').val(finalResult);
            }
        }
    };
});
var recognition2 = new webkitSpeechRecognition();
recognition2.continuous = true;
recognition2.lang = "es";
$('#search_input2').click(function(event) {
    recognition.start();
});
recognition2.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input2').val(finalResult);
        }
    }
};

//input3
$(document).ready(function() {
    var recognition3 = new webkitSpeechRecognition();
    recognition3.continuous = true;
    recognition3.lang = "es";
 
    $('#search_input3').click(function(event) {
        recognition3.start();
    });
 
    recognition3.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input3').val(finalResult);
            }
        }
    };
});
var recognition3 = new webkitSpeechRecognition();
recognition3.continuous = true;
recognition3.lang = "es";
$('#search_input3').click(function(event) {
    recognition3.start();
});
recognition3.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input3').val(finalResult);
        }
    }
};

//input4
$(document).ready(function() {
    var recognition4 = new webkitSpeechRecognition();
    recognition4.continuous = true;
    recognition4.lang = "es";
 
    $('#search_input4').click(function(event) {
        recognition4.start();
    });
 
    recognition4.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input4').val(finalResult);
            }
        }
    };
});
var recognition4 = new webkitSpeechRecognition();
recognition4.continuous = true;
recognition4.lang = "es";
$('#search_input4').click(function(event) {
    recognition4.start();
});
recognition4.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input4').val(finalResult);
        }
    }
};

//input5
$(document).ready(function() {
    var recognition5 = new webkitSpeechRecognition();
    recognition5.continuous = true;
    recognition5.lang = "es";
 
    $('#search_input5').click(function(event) {
        recognition5.start();
    });
 
    recognition5.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input5').val(finalResult);
            }
        }
    };
});
var recognition5 = new webkitSpeechRecognition();
recognition5.continuous = true;
recognition5.lang = "es";
$('#search_input5').click(function(event) {
    recognition5.start();
});
recognition5.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input5').val(finalResult);
        }
    }
};

//input6
$(document).ready(function() {
    var recognition6 = new webkitSpeechRecognition();
    recognition6.continuous = true;
    recognition6.lang = "es";
 
    $('#search_input6').click(function(event) {
        recognition6.start();
    });
 
    recognition6.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input6').val(finalResult);
            }
        }
    };
});
var recognition6 = new webkitSpeechRecognition();
recognition6.continuous = true;
recognition6.lang = "es";
$('#search_input6').click(function(event) {
    recognition6.start();
});
recognition6.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input6').val(finalResult);
        }
    }
};

//input7
$(document).ready(function() {
    var recognition7 = new webkitSpeechRecognition();
    recognition7.continuous = true;
    recognition7.lang = "es";
 
    $('#search_input7').click(function(event) {
        recognition7.start();
    });
 
    recognition7.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input7').val(finalResult);
            }
        }
    };
});
var recognition7 = new webkitSpeechRecognition();
recognition7.continuous = true;
recognition7.lang = "es";
$('#search_input7').click(function(event) {
    recognition7.start();
});
recognition7.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input7').val(finalResult);
        }
    }
};

//input8 
$(document).ready(function() {
    var recognition8 = new webkitSpeechRecognition();
    recognition8.continuous = true;
    recognition8.lang = "es";
 
    $('#search_input8').click(function(event) {
        recognition8.start();
    });
 
    recognition8.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input8').val(finalResult);
            }
        }
    };
});
var recognition8 = new webkitSpeechRecognition();
recognition8.continuous = true;
recognition8.lang = "es";
$('#search_input8').click(function(event) {
    recognition8.start();
});
recognition8.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input8').val(finalResult);
        }
    }
};

//input9
$(document).ready(function() {
    var recognition9 = new webkitSpeechRecognition();
    recognition9.continuous = true;
    recognition9.lang = "es";
 
    $('#search_input9').click(function(event) {
        recognition9.start();
    });
 
    recognition9.onresult = function (event) {
        finalResult = '';
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalResult = event.results[i][0].transcript;
                $('#search_input9').val(finalResult);
            }
        }
    };
});
var recognition9 = new webkitSpeechRecognition();
recognition9.continuous = true;
recognition9.lang = "es";
$('#search_input9').click(function(event) {
    recognition9.start();
});
recognition9.onresult = function (event) {
    finalResult = '';
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            finalResult = event.results[i][0].transcript;
            $('#search_input9').val(finalResult);
        }
    }
};