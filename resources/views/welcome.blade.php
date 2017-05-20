<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Word2Vec</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Rubik:100,600" rel="stylesheet" type="text/css">
        <!-- Styles -->
        <style>
        html, body {
        padding-top: 2em;
        background-color: #fff;
        color: #636b6f;
        font-family: 'Rubik', sans-serif;
        font-weight: 100;
        margin: 0;
        }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    {{ Form::open(array('url' => 'retrieved')) }}
                    <h3>Slang Word</h3>
                    <div class="form-group">
                        {{ Form::text('slang_word', null, array('class' => 'form-control', 'placeholder' => 'input slang word')) }}
                    </div>
                    <p>{{ Form::submit('Submit!', array('class' => 'btn btn-primary')) }}</p>
                    {{ Form::close() }}
                    @if (session('hasil'))
                    <h3>Kata: <span style="font-weight: 600">{{ session('query') }}</span></h3>
                    <h4 style="font-weight: 600; color: #00796b">{{(session('stat'))}}</h4>
                    <br>
                    <table class="table">
                        <tbody>
                            @foreach (session('hasil') as $kata)
                            <tr>
                                <td>
                                    {{ $kata }}
                                </td>
                            </tr>
                            @endforeach
                        </tbody>
                    </table>
                    @endif
                </div>
                <div class="col-md-9">
                    @if (session('hasil'))
                    <br>
                    <script type="text/javascript" src="https://ssl.gstatic.com/trends_nrtr/1015_RC10/embed_loader.js"></script> <script type="text/javascript"> trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"{{ session('query') }}","geo":"ID","time":"today 5-y"}],"category":0,"property":""}, {"exploreQuery":"geo=ID&q={{ session('query') }}","guestPath":"https://trends.google.com:443/trends/embed/"}); </script>
                    @endif
                </div>
            </div>
        </div>
        
        
    </body>
</html>