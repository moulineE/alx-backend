import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';
const kue = require('kue');
const queue = kue.createQueue();

before(function () {
  queue.testMode.enter();
});

afterEach(function () {
  queue.testMode.clear();
});

after(function () {
  queue.testMode.exit();
});
it('should create jobs correctly', function (done) {
  const jobs = [
    { phoneNumber: '1234567890', message: 'Hello!' },
    { phoneNumber: '0987654321', message: 'Goodbye!' }
  ];

  createPushNotificationsJobs(jobs, queue);

  queue.process('push_notification_code_3', function (job, done) {
    expect(job.data).to.have.property('phoneNumber');
    expect(job.data).to.have.property('message');
    done();
  });

  queue.on('job complete', function (id, _result) {
    kue.Job.get(id, function (_err, _job) {
      if (queue.testMode.jobs.length === jobs.length) {
        done();
      }
    });
  });
});
