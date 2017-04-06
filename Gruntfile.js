module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt);

    grunt.initConfig({
        sass: {
            dist: {
                src: "src/sass/style.scss",
                dest: "css/style.css"
            }
        },

        watch: {
            sass: {
                files: "src/sass/" + "**/*.scss",
                tasks: ['sass']
            }
        },

        cssbeautifier: {
            files: ["css/style.css"],
            options: {
                indent: '  ',
                openbrace: 'end-of-line',
                autosemicolon: true
            }
        }
    });

    grunt.registerTask('default', [
        'sass','cssbeautifier'
    ]);

     grunt.registerTask('watch', [
        'watch'
    ]);


}